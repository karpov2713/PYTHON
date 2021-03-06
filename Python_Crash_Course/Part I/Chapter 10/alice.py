# filename = 'text_files'

"""
with open(filename, encoding='utf-8') as f:
    contents = f.read()
"""

"""
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
"""

"""
АНАЛИЗ ТЕКСТА
"""

"""
title = "Alice in Wonderland"
title.split()
print(title.split())
"""

"""
filename = 'text_files/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} doesn't exist.")
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
"""

