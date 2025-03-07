

import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

text = "Contact Prachi.doe@example.com, patil_doe123@domain.org for more details."
print(extract_emails(text)) 
