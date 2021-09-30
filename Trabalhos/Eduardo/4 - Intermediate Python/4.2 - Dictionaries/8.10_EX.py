def browseCharacter(string):
    dictionary = {}
    for char in string:
        if dictionary.get(char):
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

input_str = input('Enter a sentence: ')
print(browseCharacter(input_str))