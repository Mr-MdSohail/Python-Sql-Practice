        #STRING METHODS
name = "mohammed Sohail"
print(len(name)) #prints length of string
print(name.upper()) #prints whole string in CAPITAL alphabets
print(name.lower()) #prints whole string in lower alphabets
print(name.capitalize()) #prints string with just first letter capital
print(name.title()) #prints string with each first letter of each word is capital
print(name.split())  #splits all words of the string and prints it 
print(name.replace('Sohail', 'unknown')) #replaces one word with another word
print(name.find("Sohail")) #finds the string and prints the string place
print(name.isalpha()) #prints true if string contains ONLY alphabets and false even if it contains only one number