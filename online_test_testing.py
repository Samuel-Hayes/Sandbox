d = {'a': 123, 'b': 234}

d['a'] += 1
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))


print(d.get(2))


d = {'a': 3, 'b': 2, 'c': 1}
for k in sorted(list(d.keys())):
    print(k, d[k], sep='', end='')

