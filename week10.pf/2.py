a = {"aswa", "izza", "maryam"}
b = {8, 24, 4}
c = {1, "cat", 2, "dog", (1,2,3)}
a.update(b)
print(a)
b.update(a)
print(b)


a = {"aswa", "izza", "maryam"}
b = {8, 24, 4}
c = {1, "cat", 2, "dog", (1,2,3)}
print(set.union(a,b,c))
print(set.intersection(a,b,c))
print(type(set.intersection(a,b,c)))

