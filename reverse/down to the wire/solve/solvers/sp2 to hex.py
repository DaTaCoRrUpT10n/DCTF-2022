
sp2log = r"C:\Users\IS\Videos\2022-12-13 11-10-02\solve\first step.txt"


lines = open(sp2log).readlines()

out = open("out.txt","w")
print(lines)
for l in lines:
    if len(l.strip())<1:
        continue
    if l.__contains__("rel"):
        out.write("rel\n")
    elif l.__contains__("e"):
        out.write("e\n")
    else:
        print(l.strip())
        print(hex(int(l[1:9][::-1],2))[2:])
        out.write(hex(int(l[1:9][::-1],2))[2:]+"\n")

