import random

# extract_words
f = open('words.txt', 'r')
message = f.read()
words_nul = message.split("\n")
f.close()

# choice_word
word = random.choice(words_nul)
print(word)

# print_underscore
new_word = ""
end = len(word)
for i in range(0, end):
    new_word += "_"

print("Le mot à deviner est:")
print()
print(new_word)

# good_letter
