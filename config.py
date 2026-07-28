from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    test_data: TestDataConfig
    http_client: HTTPClientConfig
