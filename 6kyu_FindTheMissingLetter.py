def find_missing_letter(chars):
    startingLetter = chars[0]
    nextAlphabetLetter = chr(ord(startingLetter) + 1)
    for i, c in enumerate(chars):
        if c == nextAlphabetLetter:
            nextAlphabetLetter = chr(ord(startingLetter) + (i + 1))
    return nextAlphabetLetter