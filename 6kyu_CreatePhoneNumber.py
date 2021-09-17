def create_phone_number(n):
    l = ''.join([str(int) for int in n])
    return f'({l[:3]}) {l[3:6]}-{l[6:]}'