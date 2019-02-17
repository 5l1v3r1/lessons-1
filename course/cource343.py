infile = 'in343.txt'
outfile = 'out343.txt'
count = 0
sall = [0,0,0]
with open(infile,'r') as inf:
    for line in inf:
        words = [word for word in line.strip().split(';')]
        spersonal = 0
        count += 1
        for ind in range(len(words)):
            if ind == 0: continue
            spersonal += int(words[ind])
            sall[ind - 1] += int(words[ind])
        print(spersonal/3)
for elem in sall:
    print(elem/count,end=' ')