import random

#This function shuffles all of the characters of a string


def shuffle(string):
	tempList = list(string)
	random.shuffle(tempList)
	return ''.join(tempList)

#Main program


uppercaseletter1=chr(random.randint(65,90)) #Uses ASCII code to generate a random uppercase letter
uppercaseletter2=chr(random.randint(65,90))
lowercaseletter1=chr(random.randint(97,123)) #Generates random lowercase letter
lowercaseletter2=chr(random.randint(97,123))
number1=chr(random.randint(48,58)) #Generates random number between 0-9
number2=chr(random.randint(48,58))
specialcharacter1=chr(random.randint(33,43)) #Uses ASCII code to generate a random special character
specialcharacter2=chr(random.randint(33,43))

#Generate a password using all of the above generated characters, then put them in a random order


password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + number1 + number2 + specialcharacter1 + specialcharacter2
password = shuffle(password)

#The final output


print(password)












