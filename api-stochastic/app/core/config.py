from pydantic_settings import BaseSettings, SettingsConfigDict


# lo que hacemos que sacar
# como atributos nuestras
# configuracinoes en .env
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")


# variable que pueden usar todos los que importen
# al modulo
settings = Settings()
