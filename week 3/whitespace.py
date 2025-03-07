

import re

def replace_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()
text = "This    is    a   test  string.     "
print(replace_whitespace(text))  

