from datetime import datetime

def get_clock() -> str:
    return f"{datetime.now().hour}:{datetime.now().minute:02}"

def get_date() -> str:
    return f"{datetime.now().strftime('%d. %B')}"

def get_weekday() -> str:
    return f"{datetime.now().strftime('%A')}"

def get_minute() -> int:
    return datetime.now().minute
