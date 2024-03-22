sentence = input("Enter your sentence: ")
length_sen = len(sentence)
list_char = list(sentence[0:length_sen])
dictionary_of_words = {}
for i in list_char:
    char_count = list_char.count(i)
    dictionary_of_words.update({(i) : char_count})
print(dictionary_of_words)