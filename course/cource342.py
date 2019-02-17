infile = 'in342.txt'
outfile = 'out342.txt'
d = {}
with open(infile,'r') as inf:
    for line in inf:
        words = [str(word).lower() for word in line.strip().split()]
        for key in words:
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
m = 0
for val in d.values():
    if val > m:
        m = val
for key in d:
    if d[key] == m:
        print(key, d[key])