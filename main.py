import random
words_nul = ""
word = ""


def extract_words():
    f = open('words.txt', 'r')
    message = f.read()
    global words_nul
    words_nul = message.split("\n")
    f.close()


def choice_word():
    global word
    word = random.choice(words_nul)
    print(word)


def print_underscore():
    new_word = ""
    end = len(word)
    for i in range(0, end):
        new_word += "_"

    print("Le mot à deviner est:")
    print()
    print(new_word)


extract_words()
choice_word()
print_underscore()
