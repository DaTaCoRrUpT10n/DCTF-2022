dict ={

    '1': 0x16,
    '2': 0x1e,
    '3': 0x26,
    '4': 0x25,
    '5': 0x2e,
    '6': 0x36,
    '7': 0x3d,
    '8': 0x3e,
    '9': 0x46,
    '0': 0x45,
    '-': 0x4e,
    '_': 0x4e,
    'a': 0x1c,
    'b': 0x32,
    'c': 0x21,
    'd': 0x23,
    'e': 0x24,
    'f': 0x2b,
    'g': 0x34,
    'h': 0x33,
    'i': 0x43,
    'j': 0x3b,
    'k': 0x42,
    'l': 0x4b,
    'm': 0x3a,
    'n': 0x31,
    'o': 0x44,
    'p': 0x4d,
    'q': 0x15,
    'r': 0x2d,
    's': 0x1b,
    't': 0x2c,
    'u': 0x3c,
    'v': 0x2a,
    'w': 0x1d,
    'x': 0x22,
    'y': 0x35,
    'z': 0x1a,
    '{': 0x54,
    '}': 0x5b,
    'key.enter':0x5a,
    'key.shift': 0x12,
    'key.left': 0xe06b,
    'key.right': 0xe074,
    'key.backspace': 0x66,
}

sp2log = r"out.txt"


lines = open(sp2log).readlines()

out = open("out2.txt","w")
p=""
print(lines)
for l in lines:
    if len(l.strip())<1:
        continue
    if l.__contains__("rel"):
        out.write("rel\n")
    elif l.strip() == "e":
        out.write("e\n")
    else:
        if p == "e":
            value = {i for i in dict if dict[i] == 0xe000+int(l.strip(), 16)}
        else:
            value = {i for i in dict if dict[i] == int(l.strip(),16)}
        print(value)
        out.write(str(value)+"\n")

    p = l.strip()
