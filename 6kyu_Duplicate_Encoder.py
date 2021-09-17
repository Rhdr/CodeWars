def duplicate_encode(word):
    word = word.lower()
    retval = ''
    for c in word:
        if word.count(c) > 1:
            retval += ')'
        else:
            retval += '('
    return retval