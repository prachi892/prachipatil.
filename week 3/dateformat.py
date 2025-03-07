

import re
from datetime import datetime

def is_valid_date(date):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$'
    if not re.match(pattern, date):
        return False
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False

date1 = "15-04-2023"
date2 = "31-02-2023"

print(is_valid_date(date1))  # 
print(is_valid_date(date2))  

