string = "AABBACCDDBDE"
freq_dict = {}

for char in string:
    freq_dict[char] = freq_dict.get(char, 0) + 1

# Output: {'A': 3, 'B': 3, 'C': 2, 'D': 3, 'E': 1}
print(freq_dict)
