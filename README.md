## Where to go 
Этот проект -- это сайт с картой интересных мест в Москве.
Он создан для того, чтобы помогать людям находить интересные места в Москве.
На карте отмечены точки, кликнув на которые можно перейти к описанию места.

### Запуск проекта 
1. Склонируйте репозиторий.
2. Создайте виртуальное окружение(не меньше чем Python 3.11)
```bash
python3.11 -m venv venv
```
И запустите его
```bash
source venv/bin/activate    #Linux/macOS
venv\Scripts\activate       #Windows
```
3. Установите зависимости.
```bash
pip install -r requirements.txt
```
4. Настройте переменные окружения. Создайте файл `.env` в корне проекта. Добавьте его в `.gitignore`, чтобы секретные данные не попали в репозиторий.
Пример содержимого файла `.env`
```
DEBUG=True
SECRET_KEY='Ваш_секретный_ключ'
ALLOWED_HOSTS=['127.0.0.1', 'localhost']
```
#### Пояснение к переменным окружения
- DEBUG -- это режим отладки.
`DEBUG=True` включён во время разработки. Показывает подробные ошибки, Django сам раздаёт статику.
`DEBUG=False` включать на боевом сервере. Ошибки скрыты, статику должен отдавать веб-сервер.
`Никогда не оставляйте DEBUG=True на сервере для пользователей!`

- SECRET_KEY -- уникальный секретный ключ.
Если ключ утечёт, злоумышленник сможет подделать данные.
[Подробнее](https://docs.djangoproject.com/en/5.2/topics/signing/)

- ALLOWED_HOSTS -- это список доменных имен, для которых ваш сайт может работать, 
и это важная мера безопасности для защиты от атак, когда злоумышленник пытается направить ваш сайт на свой домен. [Подробнее](https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts)

5. Примените миграции.
```bash
python manage.py migrate
```
6. Запустите сервер.
```bash
python manage.py runserver
```
[Откройте](http://127.0.0.1:8000/places)
### Загрузка места через терминал
Вы можете добавить новое место в базу данных прямо через терминал. Вместо этого адреса вы можете поставить свой.
```bash
python manage.py load_place --url https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%BA%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B2%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9%20%D0%BD%D0%B0%2060-%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0-%D0%A1%D0%B8%D1%82%D0%B8.json
```
Источник данных для адресов должен быть записан c подробными сведениями о локации. В поле `'imgs'` прикреплены ссылки на картинки, которые должны быть в формате `.jpg`.
Формат должен быть такой:
```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

### Пример того, как должна выглядит карта:
<img width="1536" height="955" alt="image" src="https://github.com/user-attachments/assets/3f9af98c-113b-4cb9-be82-fa82e30a6a78" />
