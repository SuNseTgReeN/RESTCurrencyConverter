# RESTCurrencyConverter
Цель проекта "Конвертер валют" - создать конвертер валют, который собирает данные с сайта [https://www.cbr-xml-daily.ru/daily_json.js](https://app.currencyapi.com)
и переводит одну валюту в другую.
### Параметры запроса:
    - base_currency (обязательный): код валюты, из которой производится конвертация.
    - currencies (обязательный): код валюты, в которую производится конвертация.
    - many (опциональный): значение, которое необходимо конвертировать. По умолчанию 0.
    - apikey (обязательный): ключ API, который можно получить на сайте https://app.currencyapi.com

### Пример запроса:
    GET /api/rates/?base_currency=USD&currencies=RUB&value=1&apikey=API_KEY
    
### Пример ответа:
    {
    "base_currency": "USD",
    "currencies": "RUB",
    "many": 5.0,
    "data": 483.517204673
    }
### Установка и запуск
1. Скопировать репозиторий git clone https://github.com/SuNseTgReeN/RESTCurrencyConverter
2. Создать виртуальное окружение и установить все зависимости из requirements.txt
3. Переименовать файл .env.example в .env и прописать в нём SECRET_KEY, API_KEY 
4. Запустите приложение используя команду `python3 manage.py runserver`
5. Перейдите по ссылке из примера
6. Вы великолепны!
