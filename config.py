from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_HOST = os.getenv("APP_HOST")
    APP_PORT = int(os.getenv("APP_PORT"))
    APP_RELOAD = os.getenv("APP_RELOAD")

    POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))  # default 5432
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")

    @property
    def database_url(self):
        return (
            f"postgresql://{self.POSTGRES_USERNAME}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"
        )

settings = Settings()
