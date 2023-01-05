# Я художник - я так вижу
Легко можно рисовать нулями и единицами, если знаешь из чего состоит цвет.

![image](https://user-images.githubusercontent.com/65303418/210699683-6f40dd5f-8e42-4ef1-92eb-47d811afc608.png)
* Cчитываем RGB каждого пикселя
* Далее переводим значение каждого из цветов в бинарный вид
* Записываем результат в файл
* Открываем текстовый редактор и получаем картинку с заветным флагом!
![image](https://user-images.githubusercontent.com/65303418/210699661-214b4177-40e4-4920-ad33-32b05cd784ca.png)

Решение на python:
```
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
```
