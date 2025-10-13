from agent import WorkflowInput, run_workflow
import asyncio

async def _demo_call():
    result = await run_workflow(WorkflowInput(input_as_text="What is diagonal panel?"))
    if hasattr(result, "output_text"):
        print(result.output_text)
    else:
        print(result)

asyncio.run(_demo_call())