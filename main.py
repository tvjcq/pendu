import random
words_nul = ""
word = ""
new_word = ""
g_letter = []
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
    global new_word
    end = len(word)
    for i in range(0, end):
        new_word += "_"

    print("Le mot à deviner est:")
    print(new_word)

def good_letter(w, l):
    global g_word
    global g_letter
    g_letter = g_letter
    nch = list(g_word)
    letter = list(w)
    max = len(w)
    for i in range(0, max):
        if letter[i] == l:
            nch[i] = l
        elif l in g_letter:
            nch[i] = nch[i]
            print("Tu l'a déjà dit")
            break
        else:
            nch[i] = nch[i]
    g_word = "".join(nch)
    g_letter += [l]
    return g_word


extract_words()
choice_word()
print_underscore()

g_word = new_word

while g_word != word:
    print()
    letter = input("Votre lettre : ")
    print(good_letter(word, letter))
