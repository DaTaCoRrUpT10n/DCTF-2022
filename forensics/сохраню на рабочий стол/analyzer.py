def Hex(integer):
    return "{:x}".format(integer).upper()

def decode_ascii(data):
    data = bytes([i if 32<=i<=126 else 46 for i in data])
    return data.decode(encoding="ascii", errors="replace")

def print_hex_style(data, start = 0):
    for i in range(0,len(data),16):
        snip = data[i:i+16]
        print("{:08x}".format(start+i).upper() + "| "+snip.hex().upper() + " |"+ decode_ascii(snip))

f = open("desktop.reg",encoding="UTF-16")
lines = f.readlines()

#позиция потом номер иконки в списке всех
#порядок как в именах
#все позиции идут после названий

#скорее всего 4-байтовые значения float

IconLayoutsHex = ""
collect = False
for i in lines:
    if i.__contains__('"'):
        collect = False
    if collect ==True:
        IconLayoutsHex +=i.split("\\")[0].strip()
    if i.__contains__('IconLayouts"=hex:'):
        collect = True
        IconLayoutsHex+=i.split('IconLayouts"=hex:')[1].split("\\")[0].strip()



IconLayoutsHex = IconLayoutsHex.replace(",","").strip()
print(IconLayoutsHex)
data = bytes.fromhex(IconLayoutsHex)

f = open("data.dat","wb")
f.write(data)

print_hex_style(data)
f.close()


f = open('data.dat','rb').read()

f = f[0x1AD0:]

print(f)

import struct

X = []
Y = []
labels = []
for i in range(119):
    flt = f[0:8]
    f = f[8:]
    id = f[0:1]
    f = f[2:]

    [x,y] = struct.unpack('2f',flt)
    print(x,y,int.from_bytes(id, "big"))
    X.append(x)
    Y.append(y)
    labels.append(int.from_bytes(id, "big"))


# importing the required module
import matplotlib.pyplot as plt
plt.gca().invert_yaxis()
# plotting the points
plt.scatter(X, Y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Desktop')

#for i, txt in enumerate(labels):
#    plt.annotate(txt, (X[i], Y[i]))

# function to show the plot
plt.show()
