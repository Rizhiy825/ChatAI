# ui.py — ultra-simple chat UI for your agent (MVP)
# Usage:
#   1) pip install -r requirements.txt
#   2) copy .env.example to .env and set OPENAI_API_KEY
#   3) python mvpUI.py
#   4) open http://127.0.0.1:7860

import os
from dotenv import load_dotenv
import gradio as gr

# Load environment variables
load_dotenv()

# Import your agent entrypoint
from agent import run_workflow, WorkflowInput

# Chat handler: takes the latest user message, calls your agent, returns text
async def respond(message: str, history: list[tuple[str, str]]):
    try:
        result = await run_workflow(WorkflowInput(input_as_text=message))
        return result.get("output_text", "(Пустой ответ от агента)")
    except Exception as e:
        return f"Ошибка: {e}"

# Minimalistic Gradio chat app
chat = gr.ChatInterface(
    fn=respond,
    title="SmartWOP Agent — Chat (MVP)",
    description="Enter a query. The agent responds only based on the found content.",
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    chat.launch(server_name="0.0.0.0", server_port=port, show_error=True, share=True)
