# SmartWOP Chat AI - RAG Agent

Чат-агент для работы с базой знаний SmartWOP через OpenAI Agents API с векторным поиском.

## 🚀 Быстрый старт

### 1. Установка зависимостей

```powershell
# Активация виртуального окружения
.\.venv\Scripts\Activate.ps1

# Установка зависимостей
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Скопируйте файл `.env.example` в `.env` и укажите ваш API ключ:

```powershell
Copy-Item .env.example .env
```

Откройте `.env` и установите:
```bash
OPENAI_API_KEY=sk-ваш-реальный-ключ-здесь
```

### 3. Проверка установки

```powershell
python check_setup.py
```

### 4. Запуск приложения

```powershell
python mvpUI.py
```

Откройте http://127.0.0.1:7860 в браузере.

## 📁 Структура проекта

```
ChatAI/
├── agent.py              # Основной модуль агента с интеграцией OpenAI
├── mvpUI.py              # Gradio веб-интерфейс
├── check_setup.py        # Скрипт проверки окружения
├── .env                  # Конфигурация (не коммитить в git!)
├── .env.example          # Шаблон конфигурации
├── requirements.txt      # Зависимости проекта
├── README.md             # Полная документация
├── QUICKSTART.md         # Краткое руководство
└── START_HERE.md         # Быстрая справка
```

## 🔧 Конфигурация

### Переменные окружения (.env)

```bash
# OpenAI API
OPENAI_API_KEY=sk-your-key-here

# UI порт
PORT=7860
```

## 📦 Зависимости

- `openai` - OpenAI API клиент
- `agents` - OpenAI Agents framework
- `gradio` - Веб-интерфейс
- `pydantic` - Валидация данных
- `python-dotenv` - Работа с .env файлами

Полный список см. в `requirements.txt`

## 💡 Использование

### Запуск Web UI

```powershell
python mvpUI.py
```

### Примеры вопросов

- "What is diagonal panel?"
- "How do I use separators?"
- "Explain the woodWOP component"

## 🛠️ Разработка

### Структура агента

Агент использует OpenAI Agents API с:
- Векторным хранилищем для поиска контекста
- GPT-5-nano модель для генерации ответов
- Reasoning effort: minimal для быстрых ответов

### Модификация промпта

Промпт системы находится в `agent.py` в функции `summarize_and_display_instructions`.

## 📝 Лицензия

Проект для внутреннего использования.
