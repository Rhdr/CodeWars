def likes(names):
    count = len(names)

    retval = ''
    if count == 0:
        retval = 'no one likes this'
    elif count == 1:
        retval = f'{names[0]} likes this'
    elif count == 2:
        retval = f'{names[0]} and {names[1]} like this'
    elif count == 3:
        retval = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        retval = f'{names[0]}, {names[1]} and {count-2} others like this'
    return retval