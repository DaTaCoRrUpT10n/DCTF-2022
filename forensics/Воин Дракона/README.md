# Краткая инструкция:
 
* Открыть файл KaliLinux, изменив Имя vm на KaliLinux
* Видим, что изображение grub не стандартное
* Загружаемся и вводим логин:kali и пароль:kali
* Далее найдём изображение, для этого выполним grep -r .jpg из католога /etc/,где находим splash.jpg
* Командой sudo steghide extract -sf default/grub.d/splash.png, используя пароль:kali извлекаем файл DragonWarrior
* Открыть файл
* Получить флаг
