tbl = {}
with open('in375.txt','r') as inf:
        for line in inf:
            words = [word for word in line.strip().split('\t')]
            print(words[0],words[2])
            if int(words[0]) not in tbl:
                tbl[int(words[0])] = [0,0]
            tbl[int(words[0])][0] += int(words[2])
            tbl[int(words[0])][1] += 1
m = 0
for key in tbl:
    if key > m:
        m = key
for ind in range(1,m+1):
    if ind not in tbl:
        print(ind, '-')
    else:
        print(ind, tbl[ind][0] / tbl[ind][1])