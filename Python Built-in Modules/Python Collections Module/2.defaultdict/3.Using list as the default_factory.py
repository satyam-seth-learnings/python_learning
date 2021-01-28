from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dd = defaultdict(list)
for k, v in s:
    dd[k].append(v)
print(dd)
print(sorted(dd.items()))
d = dict()
for k, v in s:
    d.setdefault(k, []).append(v)
print(d)
print(sorted(d.items()))