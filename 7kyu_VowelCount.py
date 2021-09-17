def get_count(input_str):
    num_vowels = 0
    vowelLst = 'aeiou'
    for s in input_str:
        if s in vowelLst:
            num_vowels += 1
    return num_vowels


def get_count(input_str):
    input_str = str(input_str)
    num_vowels = 0
    vowelLst = ['a', 'e', 'i', 'o', 'u']
    for s in input_str:
        if s in vowelLst:
            num_vowels += 1
    return num_vowels