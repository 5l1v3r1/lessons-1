def plus(i):
    return i + 10

si = [2,4,7]

n_si = map(plus, si)

print(n_si)
print(list(n_si))


# def map(func, itterable):
#     for i in itterable:
#         yield func(i)

n1_si = map (lambda i: i + 12, si)
print(list(n1_si))

n2_si = [i + 33 for i in si]
print(n2_si)

print('*'*20)
s_si = ['Petya', 'Vasya', 'Gena']

def is_y(string):
    return 'y' in string.lower()

s_sf_filt = filter(is_y, s_si)
print(s_sf_filt)
print(list(s_sf_filt))

s_sf_filt = filter(lambda string: 'y' in string.lower(), s_si)
print(s_sf_filt)
print(list(s_sf_filt))

s_sf_filt = [string for string in s_si if 'y' in string.lower()]
print(s_sf_filt)