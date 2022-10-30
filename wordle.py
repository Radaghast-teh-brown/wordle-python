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

# Typing area--------------------------------------------------------
answer = ["-","-","-","-","-"]
for i in range(6):
    word = input("This is your {d}° chance: ".format(d = i+1))
    verify = True
    while verify:
        if len(word) != 5 or not(word.isalpha()):
            word = input("Invalid word. Type again: ")
        else:
            verify = False



