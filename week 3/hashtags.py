

import re

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

text = "Loving the weather today! #sunny #goodvibes #relax"
print(extract_hashtags(text))  

