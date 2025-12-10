import argparse
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from dotenv import load_dotenv
load_dotenv()

def send_message(token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    resp = requests.post(
        url,
        json={"chat_id": chat_id, "text": text},
        verify=False,        # отключаем проверку SSL
        timeout=15
    )

    return resp

def main():
    parser = argparse.ArgumentParser(description="Отправить текстовый файл или сообщение в Telegram-чат через Bot API")
    parser.add_argument("--file", "-f", help="Путь к .txt файлу с текстом сообщения")
    parser.add_argument("--text", "-t", help="Текст сообщения, введённый напрямую из терминала")
    parser.add_argument("--token", help="Токен бота")
    parser.add_argument("--chat_id", help="ID чата")
    args = parser.parse_args()

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("\nОшибка: не указан токен или chat_id.\n")
        print("Укажите их так:")
        print("  python send.py --text 'Привет' --token 123:ABC --chat_id 987654321\n")
        print("Или установите переменные окружения:")
        print("  export TELEGRAM_BOT_TOKEN=123:ABC")
        print("  export TELEGRAM_CHAT_ID=987654321\n")
        return

    if not args.file and not args.text:
        print("\nОшибка: нужно указать либо --file, либо --text.\n")
        print("Примеры:")
        print("  python send.py --text 'Привет!'")
        print("  python send.py --file 'message.txt'\n")
        return

    text = ""

    if args.file:
        if not os.path.exists(args.file):
            print(f"\nФайл не найден: {args.file}\n")
            print("Проверь путь. Если в пути есть пробелы — оберни его в кавычки.\n")
            return

        with open(args.file, encoding="utf-8") as f:
            text += f.read()

    if args.text:
        if text:
            text += "\n"
        text += args.text

    try:
        resp = send_message(token, chat_id, text)
        data = resp.json()

        if data.get("ok"):
            print("Сообщение успешно отправлено!")
        else:
            print("Ошибка Telegram API:", data)

    except Exception as e:
        print("\nИсключение при отправке:", e)
        print("\nПопробуйте ещё раз или проверьте интернет/прокси.\n")

if __name__ == "__main__":
    main()
