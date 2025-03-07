

import re

def is_valid_phone(phone):
    pattern = r'^👦\d{3}👦 \d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

phone1 = "(123) 456-7890"
phone2 = "123-456-7890"

print(is_valid_phone(phone1))  
print(is_valid_phone(phone2))

