data = "manik"
print(data.upper()) #retruns the string to lower case i.e manik

#ASSIGNMENT: 10 STRING METHODS

print(data.lower()) #retruns the string to lower case i.e manik

print(data.capitalize())    #retruns the first letter in upper case i.e Manik

print(data.title())         #returns the first letter of every word in upper case i.e Manik

print(data.swapcase())      #returns the lower case to upper case and vice-versa i.e MANIK

print(data.count('m'))      #counts the number of given string i.e 1

print(data.find('n'))       #returns the index of the given string i.e 2

print(data.replace('manik', 'Aashish'))     #replaces the string with another given string i.e Aashish

print(data.split('i'))          # Splits the string at the specified separator, and returns a list i.e ['man' , 'k']

print(data.startswith('m'))     #returns true if the string starts with m i.e True

print(data.startswith('M'))     #returns true if the string starts with M i.e False

print(data.isalnum())           #Returns True if all characters in the string are alphanumeric i.e True

print(data.isalpha())           #Returns True if all characters in the string are in the alphabet i.e True

print(data.islower())           #returns True if the string is in lower case i.e True

print(data.isupper())           #returns True if the string is in lower case i.e True

new_data = "My name is Aashish"

print(new_data.replace("Aashish", "Maniraj"))   #replaces the string with another given string i.e Maniraj



data2 = 'i love veg food'
print(data2.replace("veg", "non-veg"))          #OUTPUT: i love non-veg food


data3 = "aashey110@gmail.com"
split_data3 = data3.split("@")
print(split_data3)                  #OUTPUT: ['aashey' , 'gmail.com']
second_part = split_data3[1]
second_part_split = second_part.split(".")
print(second_part_split)            #OUTPUT: ['gmail', 'com']
split_data3.remove("gmail.com")       #removes gmail.com from the list
split_data3.extend(second_part_split)
print(split_data3)                      #OUTPUT: ['aashey110', 'gmail', 'com']
