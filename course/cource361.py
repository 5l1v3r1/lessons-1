import requests
with open('in361.txt','r') as inf:
    urlpage = inf.readline().strip()
page = requests.get(urlpage)
lines = page.text.splitlines()
print(len(lines))