import random

print("-"*40)
print(15*" " + "WORDLE")
print("-"*40)
print("You have six chances to guess the word.")
print("-"*40)


# Reading the file and storing the words in a list ------------------

list_of_words = list()
f = open("words.txt", "r")
for x in f:
    list_of_words.append(x.lower().replace("\n",""))
print(list_of_words)
f.close();
guess_word = list_of_words[random.randrange(0,len(list_of_words))]
print(guess_word)

# Typing area--------------------------------------------------------
answer = ["-","-","-","-","-"]
final = False
for i in range(6):
    word = input("This is your {d}° chance: ".format(d = i+1))
    verify = True
    while verify:
        if len(word) != 5 or not(word.isalpha()):
            word = input("Invalid word. Type again: ")
        else:
            verify = False
    for n in range(5):
        for k in range(5):
            if word[n] == guess_word[k]:
                answer[k] = word[n]
    print(answer)
    if word == guess_word or '-' not in answer:
        print("You won the game!")
        final = True
        break

if final == False:
    if '-' in answer:
        print("You lost the game! The word is: ", guess_word)
    else:
        print("You won the game")



            




