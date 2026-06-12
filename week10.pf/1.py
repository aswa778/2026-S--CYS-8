s = {1, 2, 3, 3}
print(s)
print(type(set()))

a = set([1, 2, 3, 4])
print(a)
print(type(a))

s = {"ce", "cs", "ee", "ce", "ai", "ee"}
for i in s:
    print(i)

s = {"ce", "cs", "ee", "ce', 'ai", "ee"}
for i in s:
    if i =="ce":
        print("ce is in the set")

s = {"ce", "cs", "ee", "ce', 'ai", "ee"}
s.add("ae")
print(s)

s = {"ce", "cs", "ee", "ce', 'ai", "ee"}
s.discard("cs")
s.discard("ce")
s.remove("ai")
print(s)

s = {"ce", "cs", "ee", "ce', 'ai", "ee"}
s.pop()
print(s)

s = {"ce", "cs", "ee", "ce', 'ai", "ee"}
s.clear()
print(s)
print(type(s))
