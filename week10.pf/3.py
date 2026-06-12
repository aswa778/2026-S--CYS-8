s1 = {1,2,3,4}
s2 = {9,4,5,6}
print(s1.union(s1,s2))
s1.update(s2)
print(s1.intersection(s1,s2))
print(s1.intersection_update(s2))

s1 = {1,2,3,4}
s2 = {9,5,6}
print(s1.isdisjoint(s2))
s = s1.difference(s2)
ss = s2.difference(s1)
print(s)
print(ss)
print(s1)
print(s2)


