import json

# Загрузка JSON (парсинг)
json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)
print(parsed_data["name"])  # Выведет: Иван

# Сохранение JSON (сериализация)
data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}
json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку, indent - форматирование
print(json_string)

# Чтение JSON из файла
with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)  # Загружаем JSON из файла
    print(read_data)

# Запись JSON в файл
with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)  # Сохраняем JSON в файл