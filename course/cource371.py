def addteam(d,name):
    if name not in d:
        d[name] = [0]*5

n = int(input())
_dict = {}
for ind in range(n):
    mlist = [word for word in input().split(';')]
    addteam(_dict,mlist[0])
    addteam(_dict,mlist[2])
    _dict[mlist[0]][0] += 1
    _dict[mlist[2]][0] += 1
    if int(mlist[1]) > int(mlist[3]):
        _dict[mlist[0]][1] += 1
        _dict[mlist[0]][4] += 3
        _dict[mlist[2]][3] += 1
        #_dict[mlist[2]][4] += 0
    elif int(mlist[1]) < int(mlist[3]):
        _dict[mlist[2]][1] += 1
        _dict[mlist[2]][4] += 3
        _dict[mlist[0]][3] += 1
        #_dict[mlist[0]][4] += 0
    else:
        _dict[mlist[2]][2] += 1
        _dict[mlist[2]][4] += 1
        _dict[mlist[0]][2] += 1
        _dict[mlist[0]][4] += 1
for key in _dict:
    print(key,end=':')
    for elem in _dict[key]:
        print(elem,end=' ')
    print()
    