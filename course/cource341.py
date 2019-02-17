infile = 'in.txt'
outfile = 'out.txt'

with open(infile,'r') as inf:
    codedtext = inf.readline().strip()
nset = {'0','1','2','3','4','5','6','7','8','9'}
letter = ''
count = 0
decodetest = ''
for let in codedtext:
    if letter!='' and let in nset: #буква есть ищем число
        count = count*10 + int(let)
    elif letter=='' and let not in nset: #буквы нет и let не цифра
        letter = let
    else:
        decodetest = decodetest + letter*count
        letter = let
        count = 0
    #print(let,letter,count)
decodetest = decodetest + letter*count

with open(outfile,'w') as inf:
    inf.write(decodetest)
#print(codedtext)
#print(decodetest)
    
    