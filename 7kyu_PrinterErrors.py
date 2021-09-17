import string


def printer_error(s):
    errorCount = 0
    azLst = list(string.ascii_lowercase)  #m at pos 12

    lastVal = None
    for i in s:
        if i > 'm':
            errorCount += 1

    return (f'{errorCount}/{len(s)}')


import string


def printer_error(s):
    s = str(s).lower()
    errorCount = 0
    azLst = list(string.ascii_lowercase)  #m at pos 12

    lastVal = None
    for i in s:
        try:
            azLst.index(i, 0, 13)
        except:
            errorCount += 1

    return (f'{errorCount}/{len(s)}')