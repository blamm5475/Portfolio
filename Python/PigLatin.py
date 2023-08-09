#This program will translate single words into Pig Latin
word = input("Please enter the word you like to translate to Pig Latin?:")
first = word[0]
rest = word[1:]
result = rest + "-" + first + "y"
print(result)