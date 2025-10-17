# SmartWOP Chat AI

Чат-агент для SmartWOP на базе OpenAI Agents API.

## ⚡ Быстрый старт

```powershell
# 1. Настройте API ключ в .env
OPENAI_API_KEY=sk-ваш-ключ

# 2. Проверьте установку
python check_setup.py

# 3. Запустите приложение
python mvpUI.py
```

Откройте http://127.0.0.1:7860

## 📚 Документация

- `README.md` - Полная документация
- `QUICKSTART.md` - Краткое руководство
- `.env.example` - Пример конфигурации

## 📦 Структура проекта

```
ChatAI/
├── agent.py           # Логика агента
├── mvpUI.py           # Gradio веб-интерфейс  
├── check_setup.py     # Проверка окружения
├── requirements.txt   # Зависимости
├── .env               # Конфигурация (ваш API ключ)
├── .env.example       # Пример конфигурации
├── README.md          # Полная документация
├── QUICKSTART.md      # Краткое руководство
└── Files/             # Дополнительные файлы
```

## 🔧 Требования

- Python 3.8+
- OpenAI API ключ
- Зависимости из `requirements.txt`
