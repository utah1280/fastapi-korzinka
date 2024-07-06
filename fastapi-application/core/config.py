from pathlib import Path
from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from dotenv import load_dotenv
load_dotenv()

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class ApiPrefix(BaseModel):
    prefix: str = "/api"
    categories: str = "/categories"
    contacts: str = "/contacts"

class AuthJWT(BaseModel):
    private_key_path: Path = Path("fastapi-application/certs/jwt_private.pem")
    public_key_path: Path = Path("fastapi-application/certs/jwt_public.pem")
    algorithm: str = "RS256"
    access_token_expire_min: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    auth_jwt: AuthJWT = AuthJWT()
    db: DatabaseConfig


settings = Settings()