n = int(input())
wokabl = set()
for ind in range(n):
    wokabl.add(input().lower())

n = int(input())
outset = set()
for ind in range(n):
    words = [str(word) for word in input().split()]
    for word in words:
        if word.lower() not in wokabl:
            if word.lower() not in outset:
                print(word)    
            outset.add(word.lower())