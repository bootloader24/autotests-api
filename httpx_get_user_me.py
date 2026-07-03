import httpx

# Формируем данные для логина
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем POST-запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

# Получаем access token из ответа
access_token = login_response.json()["token"]["accessToken"]

# Формируем заголовок с добавлением accessToken
headers = {"Authorization": f"Bearer {access_token}"}

# Выполняем GET-запрос на получение информации о своём пользователе, используя заголовок с accessToken
user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

# Выводим JSON-ответ от сервера с данными о пользователе и статус код ответа
print(user_me_response.json())
print(user_me_response.status_code)
