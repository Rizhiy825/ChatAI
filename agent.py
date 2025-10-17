import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from types import SimpleNamespace
from agents import RunContextWrapper, Agent, ModelSettings, TResponseInputItem, Runner, RunConfig
from openai.types.shared.reasoning import Reasoning
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Shared client for guardrails and file search
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ctx = SimpleNamespace(guardrail_llm=client)
class SummarizeAndDisplayContext:
  def __init__(self, workflow_input_as_text: str, input_result: str):
    self.workflow_input_as_text = workflow_input_as_text
    self.input_result = input_result
def summarize_and_display_instructions(run_context: RunContextWrapper[SummarizeAndDisplayContext], _agent: Agent[SummarizeAndDisplayContext]):
  workflow_input_as_text = run_context.context.workflow_input_as_text
  input_result = run_context.context.input_result
  return f"""You are a helpful assistant for a CAD app (SmartWOP).  
Answer ONLY using the provided context. If the answer is not in context, say you don't know.  
Prefer step-by-step, concise instructions. Keep tool/command names verbatim.
Rules: 
- Answer ONLY using the information from the context above. 
- Do NOT mention block numbers or the word 'context'.
- Do NOT show your reasoning, inner thoughts, or explanations of how you found the answer.
- Provide only the final clear instructions or factual answer. 
- Answer in the same language as the user question. 
- If the answer is not in context, say 'I don't know'. \n
Context: 
{input_result}"""
summarize_and_display = Agent(
  name="Summarize and display",
  instructions=summarize_and_display_instructions,
  model="gpt-5-nano",
  model_settings=ModelSettings(
    store=True,
    reasoning=Reasoning(
      effort="minimal"
    )
  )
)


class WorkflowInput(BaseModel):
  input_as_text: str


# Main code entrypoint
async def run_workflow(workflow_input: WorkflowInput):
  state = {

  }
  workflow = workflow_input.model_dump()
  conversation_history: list[TResponseInputItem] = [
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": workflow["input_as_text"]
        }
      ]
    }
  ]
  
  # Асинхронный поиск в векторном хранилище
  search_results = []
  async for result in client.vector_stores.search(
      vector_store_id="vs_68e4fc9fa5948191a7b26eace8b8c7d9", 
      query=workflow["input_as_text"], 
      max_num_results=5
  ):
      search_results.append({
          "id": result.file_id,
          "filename": result.filename,
          "score": result.score,
          "content": getattr(result, "content", [])
      })
  
  filesearch_result = {"results": search_results}
  
  # Формируем контекст из результатов
  context_parts = []
  for i, res in enumerate(filesearch_result["results"][:6]):
      if res.get("content"):
          context_parts.append(res["filename"])
          for content_item in res["content"][:2]:
              if isinstance(content_item, dict) and "text" in content_item:
                  context_parts.append(content_item["text"])
              elif hasattr(content_item, "text"):
                  context_parts.append(content_item.text)
          context_parts.append("\n")
  
  transform_result = {"result": "\n".join(context_parts)}
  summarize_and_display_result_temp = await Runner.run(
    summarize_and_display,
    input=[
      *conversation_history
    ],
    run_config=RunConfig(trace_metadata={
      "__trace_source__": "agent-builder",
      "workflow_id": "wf_68e4fc2fac808190956b9d82518edbbd07ef705c9c34c8a3"
    }),
    context=SummarizeAndDisplayContext(workflow_input_as_text=workflow["input_as_text"], input_result=transform_result["result"])
  )
  summarize_and_display_result = {
    "output_text": summarize_and_display_result_temp.final_output_as(str)
  }

  return summarize_and_display_result