given_list = [1, 5, 9, 6, 89, 27, 99, 35, -1, 1]

temp = 0

for i in range(len(given_list)): # len(given_list) is 10, so this loop will iterate 10 times (from i = 0 to i = 9).
    for j in range(0, len(given_list) - 1):     #len(given_list) - 1 is 9, so this loop will iterate 9 times (from j = 0 to j = 8) during each pass of the outer loop.
        if given_list[j] > given_list[j + 1]:   # Compares if 1 > 5. Returns FALSE. NO SWAP NEEDED
            temp = given_list[j]                
            given_list[j] = given_list[j + 1]
            given_list[j + 1] = temp



print(given_list)