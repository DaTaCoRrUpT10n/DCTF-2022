# Экзамен по истории
Вы успешно прогуляли весь семестр по истории. Теперь вам предстоит всё выучить и успешно сдать экзамен, иначе вас отчислят. Надеюсь вы хорошо умеете пользоваться википедией.
Чтобы начать: nc 158.160.25.3 50001
## Узнаём, что от нас требуется
* Подключаемся и узнаём, что нам требуется ответить на 300 вопросов за 2 минуты следующего формата: "When was [историческая личность] ['death'/'born']?". Например: When was Galileo Galilei death? Ответ требуется отправлять следующего формата. [день].[месяц].[год]. Например: 5.12.2001. Замечаем, что впереди дня не используется '0'. Значит незначащие нули требуется отбрасывать при отправке ответа. 
## Откуда брать данные?
* Описание предлагает для нашей задачи использовать википедию. Для более удобного парсинга страниц википедии будем использовать JSON, который можно получить по следующей ссылке: http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles= + [историческая личность] + &format=json.
Например: https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Galileo%20Galilei&format=json. Поможет нам с этой задачей  mwparserfromhell, который предназначен для парсинга Wiki. Их github: https://github.com/earwig/mwparserfromhell. Достаём значение поля birth_data/death_data в зависимости от вопроса. Удаляем незначащие нули. Ниже прилагается пример кода для поиска даты рождения.
```
def getBornDate(name):
    try:
        url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=' + name + '&format=json'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        site_json = json.loads(soup.text)
        a = (list(site_json['query']['pages'])[0])
        text = site_json['query']['pages'][a]['revisions'][0]['*']
        wiki = mwparserfromhell.parse(text)
        birth_data = wiki.filter_templates(matches="Birth date")[0]['birth_date']
        nums = re.findall(r'\d+', str(birth_data))
        date = nums[2] + "." + nums[1] + "." + nums[0]
        date = date.replace('.0', '.')
        if date[0] == '0':
            date = date[1:len(date)]
        return date
    except:
        return('Birth date not found')
```
## Как отправить данные на сервер?
* С этой задачей нам поможет справиться модуль socket в языке python. Указываем параметры и подключаемся! 
```
import socket
ip = '158.160.25.3'
port = 50001
sock = socket.socket()
sock.connect((ip, port))
```
* Чтобы получить данные нужно воспользоваться методом recv, который в качестве аргумента принимает количество байт для чтения. Мы будем читать порциями по 1024 байт. Далее обрабаытываем вопрос, получая искомую историчскую личность и какую дату требуется найти.
```
def get_question(i):
    data = sock.recv(1024).decode('utf-8')
    data = data.split(' ')
    for i in range(0,len(data)):
        if(data[i] == 'was'):
            start = i+1
        if(data[i].__contains__('born')):
            isBorn = True
            end = i
        if(data[i].__contains__('death')):
            end = i
            isBorn = False
    return ' '.join(data[start:end]), isBorn
```
* Для отправки сообщения на сервер испольуем метод send(). Отвечаем на 300 вопросов по истории и получаем наш заветный флаг! 
```
for i in range(0,301):
    info = get_question(i)
    print(info)
    if(info[1] == True):
        text = getBornDate(info[0]).encode('utf-8')
        sock.send(text)
    else:
        text = getDeathDate(info[0]).encode('utf-8')
        sock.send(text)
```
* Если вы не успеваете за 2 минуты ответить на 300 вопросов, вам поможет создание словаря с уже встреченными вопросами.
