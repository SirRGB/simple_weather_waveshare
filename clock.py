from datetime import datetime

def get_clock():
    return f"{datetime.now().hour}:{datetime.now().minute:02}"

def get_date():
    return str(datetime.now().strftime("%d. %B %Y\n"))

def get_weekday():
    return str(datetime.now().strftime("%A\n"))
