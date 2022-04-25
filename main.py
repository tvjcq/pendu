import random
import time

words_nul = ""
word = ""
new_word = ""
g_letter = []
point_verif = 0


def extract_words():
    f = open('words.txt', 'r')
    message = f.read()
    global words_nul
    words_nul = message.split("\n")
    f.close()


def choice_word():
    global word
    word = random.choice(words_nul)


def print_underscore():
    global new_word
    end = len(word)
    for i in range(0, end):
        new_word += "_"

    print("Le mot à deviner est:")
    print(new_word)


def test_letter(w, l):
    global g_word
    global g_letter
    global point_verif
    verif = g_word
    nch = list(g_word)
    letter = list(w)
    max = len(w)
    for i in range(0, max):
        if letter[i] == l:
            nch[i] = l
        elif l in g_letter:
            nch[i] = nch[i]
            print("Tu l'as déjà dit")
            break
        else:
            nch[i] = nch[i]
    g_word = "".join(nch)
    if verif != g_word:
        print("Bravo tu as trouvé une lettre !")
    elif l not in g_letter:
        print("Dommage mauvaise lettre")
        point_verif += 1
    g_letter += [l]
    return g_word


extract_words()
choice_word()
print_underscore()

g_word = new_word

while g_word != word and point_verif < 7:
    print()
    letter = input("Votre lettre : ")
    print(test_letter(word, letter))
print()

if g_word == word:
    print("Bravo tu as trouvé le mot !")
else:
    print("Dommage tu as perdu")
    print("Le mot était", word)
time.sleep(10)
