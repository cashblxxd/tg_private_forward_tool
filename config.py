from dotenv import load_dotenv
from pydantic import  BaseSettings


load_dotenv('.env')


class Settings(BaseSettings):
    API_ID: str
    API_HASH: str
    PRIVATE_CHAT_ID: int
    REDIRECT_CHAT_ID: int


settings = Settings()