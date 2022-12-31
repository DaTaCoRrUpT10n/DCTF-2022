a = set()

x = open("in.txt").read()

for z in x:
    a.add(z)

print(len(a))
print(a)


a= set()

x = open('enc.txt').read().split()
for z in x:
    a.add(z)
print(len(a))
print(a)