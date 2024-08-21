#assignment to copy list
dict = {
    'name' : 'skill shikshya',
    'location' : 'bagmati',
    'district' : 'bagmati'
}

print(dict) #prints keys and values
print(dict.keys()) #prints the keys of the dictionary
print(dict.items()) #prints the key pair data
print(dict.pop('location')) #removes the desired key
new_dict = dict.copy()
print(new_dict)



