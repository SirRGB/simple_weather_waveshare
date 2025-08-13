from datetime import datetime

def get_clock() -> str:
    return f"{datetime.now().hour}:{datetime.now().minute:02}"

def get_date() -> str:
    return str(datetime.now().strftime("%A, %d. %B"))

def get_minute() -> str:
    return f"{datetime.now().minute}"
