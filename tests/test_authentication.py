from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(public_users_client: PublicUsersClient, authentication_client: AuthenticationClient):
    # Создаем пользователя
    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    # Выполняем аутентификацию
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client.login_api(login_request)

    # Десериализуем ответ на запрос аутентификации
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # Проверяем статус-код ответа
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # Проверяем корректность тела ответа
    assert_login_response(login_response_data)

    # Проверяем, что ответ соответствует ожидаемой JSON-схеме
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
