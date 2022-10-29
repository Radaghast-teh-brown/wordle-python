print("-"*40)
print(15*" " + "WORDLE")
print("-"*40)

list_of_words = list()
f = open("words.txt", "r")
for x in f:
    list_of_words.append(x.lower().replace("\n",""))
print(list_of_words)

f.close();