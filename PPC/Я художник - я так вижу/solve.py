from PIL import Image
im = Image.open('image.png')
rgb_im = im.convert('RGB')

text = ''

for y in range(0,rgb_im.height):
	for x in range(0,rgb_im.width):
		print(y, x)
		r, g, b = rgb_im.getpixel((x, y))
		text += bin(r)[2:].zfill(8) + bin(g)[2:].zfill(8) + bin(b)[2:].zfill(8)
	text += '\n'

with open("ans.txt", "w") as f:
    f.write(text)

