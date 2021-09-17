# return masked string
def maskify(cc):
    cc = str(cc)
    retval = ''
    maskTextLength = len(cc) - 4
    for i, s in enumerate(cc):
        if i < maskTextLength:
            retval += '#'
        else:
            retval += s
    return retval