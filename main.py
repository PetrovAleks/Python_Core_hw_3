import random
import re
from datetime import datetime as dt

_MAX_NUMBER = 1000
_REGEX = r'[^0-9+]'
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Test Smith", "birthday": "1990.01.28"}
]

def get_days_from_today(date= "") -> int | Exception:
    if not date: return Exception('No date provided')

    if  isinstance(date, dt): 
        date = date.strftime('%Y-%m-%d')
        
    now = dt.now()
    try:
        delta = now - dt.strptime(date, '%Y-%m-%d')
        return abs(delta.days)
    

    except Exception as e:
        return e


def get_numbers_ticket(*args: int) -> set | Exception:
    if not args or len(args) != 3  : return Exception('Please provide 3 parameters')
    min, max, quantity  = args

    if not isinstance(min,int) or not isinstance(max,int) or not isinstance(quantity,int): return Exception("All parameters are required")
    if min >= max or min < 1: return Exception('Min number mast be less than max number and not less then 1')
    if max > _MAX_NUMBER: return Exception('Max number mast be less than 1000')
    if quantity > max - min: return Exception('Quantity mast be less than max - min')

    unicume_numbers = []
    while len(unicume_numbers) < quantity:
        new_number = random.randint(min, max)
        if new_number not in unicume_numbers:
            unicume_numbers.append(new_number)
    return sorted(unicume_numbers)

def normalize_phone(phone_number:int | str) -> int | Exception:
    if not phone_number: return Exception('No phone number provided')
    if isinstance(phone_number, int): phone_number = str(phone_number)
    phone_number = re.sub(_REGEX, '', phone_number)   
    if len(phone_number) < 9: return Exception('Phone number mast be more than 9 digits')

    if phone_number.startswith('380') and len(phone_number) == 12:
          phone_number = '+' + phone_number
    elif not phone_number.startswith('+'):
        phone_number = '+38' + phone_number      
    return phone_number

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    if not users: return []
    upcoming_birthdays = []
    for user in users:
        birthday = dt.strptime(user['birthday'], '%Y.%m.%d')
        if birthday.month == dt.now().month and birthday.day > dt.now().day and birthday.weekday()  <= 6:
            upcoming_birthdays.append(user)
    return upcoming_birthdays

print(get_days_from_today("2010-01-01"))
print(get_numbers_ticket(1, 10, 15))
print(normalize_phone("23 4567  "))
print(get_upcoming_birthdays(users))
