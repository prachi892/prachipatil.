

import re

def is_valid_url(url):
    pattern = r'^https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?$'
    return bool(re.match(pattern, url))

url1 = "https://www.example.com/path/to/page"
url2 = "ftp://example.com"

print(is_valid_url(url1))  
print(is_valid_url(url2))  
