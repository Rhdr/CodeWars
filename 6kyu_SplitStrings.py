def solution(s):
    subLst = ''
    mainLst = []
    
    if len(s) % 2 != 0:
        s += '_'
    
    for str in s:
        subLst += str
        if len(subLst) == 2:
            mainLst.append(subLst)
            subLst = ''
    
    return mainLst