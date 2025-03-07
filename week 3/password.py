

import re

def is_strong_password(password):
    pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@#$%^&+=]).{8,}$'
    return bool(re.match(pattern, password))

password1 = "Strong@123"
password2 = "weakpass"

print(is_strong_password(password1))
print(is_strong_password(password2))

