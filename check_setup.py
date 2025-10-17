"""
Скрипт проверки окружения для SmartWOP Chat AI
Запустите этот скрипт, чтобы убедиться, что все настроено правильно.
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Проверка версии Python"""
    print("🐍 Проверка версии Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - требуется Python 3.8+")
        return False

def check_env_file():
    """Проверка наличия .env файла"""
    print("\n📄 Проверка .env файла...")
    env_path = Path(".env")
    if env_path.exists():
        print("   ✅ Файл .env найден")
        return True
    else:
        print("   ❌ Файл .env не найден")
        print("   💡 Скопируйте .env.example в .env и настройте его")
        return False

def check_openai_key():
    """Проверка API ключа OpenAI"""
    print("\n🔑 Проверка OPENAI_API_KEY...")
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here" and api_key.startswith("sk-"):
        print(f"   ✅ API ключ установлен (начинается с 'sk-...')")
        return True
    else:
        print("   ❌ OPENAI_API_KEY не установлен или некорректен")
        print("   💡 Установите корректный API ключ в файле .env")
        return False

def check_dependencies():
    """Проверка установленных зависимостей"""
    print("\n📦 Проверка зависимостей...")
    required = {
        "openai": "OpenAI API клиент",
        "gradio": "Gradio для веб-интерфейса",
        "dotenv": "Python-dotenv для .env файлов",
        "pydantic": "Pydantic для валидации данных"
    }
    
    all_ok = True
    for module, description in required.items():
        try:
            if module == "dotenv":
                __import__("dotenv")
            else:
                __import__(module)
            print(f"   ✅ {description}")
        except ImportError:
            print(f"   ❌ {description} - не установлен")
            all_ok = False
    
    # Проверка openai-agents отдельно (может быть импортирован как agents)
    try:
        from agents import Agent
        print(f"   ✅ OpenAI Agents framework")
    except ImportError:
        print(f"   ❌ OpenAI Agents framework - не установлен")
        all_ok = False
    
    return all_ok

def check_main_files():
    """Проверка наличия основных файлов проекта"""
    print("\n� Проверка файлов проекта...")
    files_to_check = [
        ("agent.py", "Основной модуль агента"),
        ("mvpUI.py", "Web UI интерфейс"),
    ]
    
    all_ok = True
    for filename, description in files_to_check:
        if Path(filename).exists():
            print(f"   ✅ {description} ({filename})")
        else:
            print(f"   ❌ {description} ({filename}) - не найден")
            all_ok = False
    
    return all_ok

def main():
    print("=" * 60)
    print("🚀 SmartWOP Chat AI - Проверка окружения")
    print("=" * 60)
    
    checks = [
        check_python_version(),
        check_env_file(),
        check_openai_key(),
        check_dependencies(),
        check_main_files()
    ]
    
    print("\n" + "=" * 60)
    if all(checks):
        print("✅ Все проверки пройдены!")
        print("\n📖 Запуск приложения:")
        print("   python mvpUI.py")
        print("\n   Затем откройте http://127.0.0.1:7860 в браузере")
    else:
        print("❌ Некоторые проверки не пройдены")
        print("   Пожалуйста, исправьте указанные проблемы")
    print("=" * 60)

if __name__ == "__main__":
    main()
