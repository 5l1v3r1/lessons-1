n = int(input())
x = 0
y = 0
for ind in range(n):
    inp = [elem for elem in input().split()]
    if inp[0] == 'север':
        y += int(inp[1])
    elif inp[0] == 'восток':
        x += int(inp[1])
    elif inp[0] == 'юг':
        y -= int(inp[1])
    elif inp[0] == 'запад':
        x -= int(inp[1])
print(x,y)