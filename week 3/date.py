

import re

def extract_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    return re.findall(pattern, text)

# Example usage
text = "My birthday is on 01-07-2004 and my friend's birthday is 01-20-1990."
print(extract_dates(text))  

