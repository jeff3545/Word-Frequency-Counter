#Main Code
askFile = open(input('Enter the name of your file: '))

word_line = askFile.readlines()

askFile.close()

word_dict = {}

#add words to dictionary for function 1
for line in word_line:
    words = line.split() #seperates word
    for word in words:
        if word not in word_dict: 
            word_dict[word] = 0 
        word_dict[word] += 1


    
#Part 1 function, display concordance with function
def display_concordance(askFile):
    print('\nFile concordance Display\n')
    for word in word_dict:
        print(word,':',word_dict[word])

display_concordance(askFile)
    
#add words to lowercase dictionary for function 2
alpha = 'abcdefghijklmnopqrstuvwxyz'
lowercase_dict = {}
for character in alpha:
    words = character.split()
    for word in words:
        word = word.lower() #we need lowercase values
        if word not in lowercase_dict:
            lowercase_dict[word] = 1
        lowercase_dict[word] += 1

print("\n Part Two: \n")

#Part 2 function, displays a dictionary containing the decimal, hex, and binary representations of the lowercase char
def ascii_lowercase_letters():
    for word in lowercase_dict:
        #word.setdefault(key, [])
        lowercase_dict[word] = [ord(word),hex(ord(word)),bin(ord(word))]
    print(lowercase_dict)
            
ascii_lowercase_letters()
