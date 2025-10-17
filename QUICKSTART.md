# 🚀 Быстрый старт - SmartWOP Chat AI

## 1️⃣ Установка зависимостей

```powershell
# Активировать виртуальное окружение
.\.venv\Scripts\Activate.ps1

# Установить зависимости
pip install -r requirements.txt
```

## 2️⃣ Настройка API ключа

Откройте файл `.env` и установите ваш OpenAI API ключ:

```bash
OPENAI_API_KEY=sk-ваш-реальный-ключ-здесь
```

## 3️⃣ Проверка установки

```powershell
python check_setup.py
```

Вы должны увидеть все ✅ (галочки) - это значит всё готово!

## 4️⃣ Запуск приложения

```powershell
python mvpUI.py
```

Откройте http://127.0.0.1:7860 в браузере и начните задавать вопросы!

## ❓ Примеры вопросов

- "What is diagonal panel?"
- "How do I use separators?"
- "Explain the woodWOP component"

## 🆘 Проблемы?

Если что-то не работает:
1. Запустите `python check_setup.py`
2. Проверьте что API ключ правильный в `.env`
3. Убедитесь что виртуальное окружение активировано
4. Переустановите зависимости: `pip install -r requirements.txt`

## ✅ Готово!

Теперь вы можете задавать вопросы и получать ответы на основе базы знаний SmartWOP! 🎉
