import httpx


### Отправка GET-запроса ###
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200 (Ok)
print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


### Отправка POST-запроса ###
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью


### Отправка данных в application/x-www-form-urlencoded ###
data = {
    "username": "test_user",
    "password": "123456"
}

response = httpx.post("https://postman-echo.com/post", data=data)

print(response.status_code) # 200 (Ok)
print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}


### Передача заголовков ###
headers = {
    "Authorization": "Bearer my_secret_token"
}

response = httpx.get("https://postman-echo.com/get", headers=headers)

print(response.request.headers)
print(response.json())  # Заголовки включены в ответ


### Работа с параметрами запроса ###
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач


### Отправка файлов ###
files = {
    "file": ("example.txt", open("example.txt", "rb"))
}

response = httpx.post("https://postman-echo.com/post", files=files)

print(response.json())  # Ответ с данными о загруженном файле


### Работа с сессиями (httpx.Client) ###
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи


### Добавление базовых заголовков в Client ###
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://postman-echo.com/get")

print(response.json())  # Заголовки включены в ответ
client.close()


### Проверка статуса ответа (raise_for_status) ###
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


### Обработка таймаутов ###
try:
    response = httpx.get("https://postman-echo.com/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
