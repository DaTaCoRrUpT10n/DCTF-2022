ASCII = "_EARIOTNSLCUDPMHGBFYWKVXZJQ"

dict = {}

t = open("enc.txt").read().split()

for x in t:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1

dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1]).__reversed__()}

print(dict)
t = open("enc.txt").read()
print(len(dict.keys()))
for i in range(len(ASCII)):
    t = t.replace(list(dict.keys())[i],ASCII[i])
print(t)

t = "".join(t.split()).replace("_"," ")
print(t)

def exchange(st,L1,L2):
    temp = "\0"
    st = st.replace(L1,temp)
    st = st.replace(L2,L1)
    st = st.replace(temp,L2)
    return st

t = exchange(t,"U","C")
t = exchange(t,"A","T")
print(t)

t = exchange(t,"U","H")
print(t)


t = exchange(t,"R","A")
t = exchange(t,"U","B")
print(t)

t = exchange(t,"R","I")
t = exchange(t,"S","R")
t = exchange(t,"O","S")

print(t)

t = exchange(t,"Z","M")
t = exchange(t,"Y","G")
t = exchange(t,"K","V")
t = exchange(t,"Z","U")
t = exchange(t,"M","K")
t = exchange(t,"Z","M")
t = exchange(t,"Z","X")
t = exchange(t,"Z","Q")
t = exchange(t,"Z","J")
print(t)
