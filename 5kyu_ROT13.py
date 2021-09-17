def rot13(message):
    alphabet_dict = {}
    for i in range(97, 123):
        c = chr(i)
        i += 13
        alphabet_dict[c] = i if i < 123 else i - 26

    retval = ''
    for m in message:
        islower = m.islower()
        try:
            val = alphabet_dict[m.lower()]
            c = chr(val)
            c = c if islower else c.upper()
        except:
            c = m
        retval += c
    return retval