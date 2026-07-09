from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address  # Вложенная модель
    is_active: bool = True  # Значение по умолчанию


user = User(
    id="123",
    name='Alice',
    email='alice@example.com',
    address={
        "city": "New York",
        "zip_code": "10001"
    }
)
print(user)  # вывод всего объекта user
print(user.name)  # Alice
print(user.id)  # 123 (автоматически преобразован в int)
print(user.address.city)  # New York
print(user.model_dump_json())  # вывод в JSON
