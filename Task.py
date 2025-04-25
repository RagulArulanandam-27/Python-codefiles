import string

with open('Python-codefiles/dictionary.txt', 'r') as dict_file:
    dictionary_words = [line.strip().lower() for line in dict_file]

words_count = {word: 0 for word in dictionary_words}
# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)
with open('Python-codefiles/text.txt', 'r') as text_file:
    # text_file_words = [line.strip().lower().split() for line in text_file]
    for line in text_file:
        text_file_words = line.lower().strip().split()
        for word in text_file_words:
            words_clean = word.translate(translator)
            if words_clean in words_count:
                words_count[words_clean] += 1


for word in words_count:
    print(f'{word}: {words_count[word]}')
