"""Application configuration using environment variables."""

from pydantic_settings import BaseSettings


class MT5Config(BaseSettings):
    login: int
    password: str
    server: str

    class Config:
        env_prefix = "MT5_"
