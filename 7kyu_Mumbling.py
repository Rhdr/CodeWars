def accum(s):
    s = str(s).upper()
    retval = ''
    for pos, char in enumerate(s):
        for i in range(pos + 1):
            if i == 0:
                retval += char
            else:
                retval += char.lower()
        retval += '-'

    return retval[:-1]