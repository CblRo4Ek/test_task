# Тестовое задание

Проект для ...

---

## Структура проекта
* **mx_check.py** – проверяет список email-адресов на наличие MX-записей домена. Принимает файл с адресами. 
* **telegram_send.py** – отправляет сообщение в приватный Telegram-чат через Bot API. Принимает --text, --file, --token, --chat_id или использует переменные окружения TELEGRAM_BOT_TOKEN и TELEGRAM_CHAT_ID.
* **architecture.md** – архитектурное решение с описанием компонентов, ротации, мониторинга, распределения нагрузки, рисков и оценки стоимости.
* **example_emails.txt** и **example_message.txt** – примеры входных файлов

---

## Быстрый старт

### 1. Клонируйте или скачайте проект

```bash
git clone https://...
```

```bash
cd test_task
```

### 2. Создайте виртуальное окружение

```bash
python -m venv venv
```

### 3. Активируйте виртуальное окружение

* **Windows:**
```bash
venv\Scripts\activate
```

* **Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Установите зависимости

```bash
pip install -r requirements.txt
```

### 5. Запустите mx_check.py

```bash
python mx_check.py example_emails.txt
```
Выводит:

    <email> - домен валиден
    
    <email> - домен отсутствует
    
    <email> - MX-записи отсутствуют или некорректны
    
    <email> - некорректный формат email

### 6. Запустите telegram_send.py

Перед запуском создайте **.env** фал, в который поместите **TELEGRAM_BOT_TOKEN** и **TELEGRAM_CHAT_ID** или подавайте их напрямую в запросе:
```bash
python telegram_send.py --file example_message.txt --token <token> --chat_id <id>
```
Поддерживаются способы ввода:
* python telegram_send.py --text "текст"
* python telegram_send.py --file <file_name>.txt
* python telegram_send.py --file <file_name>.txt --text "ещё текст"

### 6. Архитектурная задача
Файл **architecture.md** содержит текстовое описание архитектуры для обслуживания 1200 email-адресов.

