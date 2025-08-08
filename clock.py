from datetime import datetime

def get_clock():
    return f"{datetime.now().hour}:{datetime.now().minute:02}"

def get_date():
    return str(datetime.now().strftime("%A %d. %B %Y"))