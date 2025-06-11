from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        converted_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('date should be in format "%Y-%m-%d"')
    
    return (datetime.today() -  converted_date).days



print(get_days_from_today('2025-06-10'))