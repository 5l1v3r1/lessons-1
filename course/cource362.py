import requests
mdir = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('in362.txt','r') as inf:
    name = inf.readline().strip()
while True:
    page = requests.get(name)
    lines = page.text.splitlines()
    print(lines[0].strip())
    if lines[0].strip()[:2] == 'We':
        print(page.text)
        break
    else:
        name = mdir + lines[0].strip()