#create dictionary
#append data to dictionary and print
#how to access and change value of dictionary
#access dictionary item using for loop

user_information = {
    "name": "Aashish Dahal",
    "age": 23,
    "city": "Kathmandu",
    "country": "Nepal",
}

information_list = ["Manik Shretha", 24, "Biratnagar", "Nepal"]
information_list.append(user_information)
print(information_list)


user_information["name"] = "Riyam Kafle"
print(user_information)


for item in user_information:
    print(user_information[item])