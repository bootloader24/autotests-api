import uuid

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel


# Вложенная модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl  # Встроенный тип
    filename: str
    directory: str


# Вложенная модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Встроенный тип
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # Вычисляемое поле
    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase для всех полей
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # default_factory для динамических значений
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(
        alias="previewFile",
        default={
            "id": "file-id",
            "url": "http://localhost:8000",
            "filename": "file.png",
            "directory": "courses"
        }
    )  # Вложенная модель
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(
        alias="createdByUser",
        default={
            "id": "user-id",
            "email": "user@gmail.com",
            "lastName": "Bond",
            "firstName": "Zara",
            "middleName": "Alise"
        }
    )  # Вложенная модель


# Инициализация модели CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Инициализация модели CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

# Инициализация модели CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
# или из json-файла
# with open("course.json", "r") as file:
#     course_json = file.read()
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)
print('Course dict:', course_json_model.model_dump())  # вывод в виде словаря
print('Course json-string:', course_json_model.model_dump_json())  # вывод в виде json-строки
print('Revert case convert:', course_dict_model.model_dump(by_alias=True))

# Демонстрация использования default_factory для динамических значений
course1 = CourseSchema()
course2 = CourseSchema()
print(course1.id)
print(course2.id)

# Использование методов и вычисляемых полей модели
user = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise"
)
print(user.get_username(), user.username)

# Обработка ошибок валидации
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())
