"""
РАБОТА С НЕСКОЛЬКИМИ ФАЙЛАМИ
"""

def count_words(filename):
    """Подсчет приблизительного количества строй в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} doesn't exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['text_files/alice.txt', 'text_files/siddhartha1.txt',
             'text_files/moby_dick.txt', 'text_files/little_women.txt']
for filename in filenames:
    count_words(filename)