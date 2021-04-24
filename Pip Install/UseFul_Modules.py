from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 6]

print(Counter(li))

sentence = 'thinking about python'
print(Counter(sentence))

dictinoary = defaultdict(lambda: 5, {'a': 1, "b": 2})
print(dictinoary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d == d2)

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d == d2)
