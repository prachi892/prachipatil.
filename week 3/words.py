

import re

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

text = "Hello, my name is Prachi patil."
print(count_words(text))  

