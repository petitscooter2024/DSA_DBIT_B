def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char != ' ': 
            freq[char] = freq.get(char, 0) + 1
    return freq

string = "data structures and algorithms"
frequencies = count_char_frequencies(string)
print("Character Frequencies:", frequencies)

