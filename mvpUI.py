# ui.py — ultra-simple chat UI for your agent (MVP)
# Usage:
#   1) pip install gradio openai pydantic
#   2) set OPENAI_API_KEY env var
#   3) python ui.py
#   4) open http://127.0.0.1:7860

import os
import gradio as gr

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
    description="Введите запрос. Агент отвечает только на основе найденного контента.",
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    chat.launch(server_name="0.0.0.0", server_port=port, show_error=True)
