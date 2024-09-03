from core.bfa_logger import BFALogger


class Settings:
    # change the url to yours 'postgresql://<user>:<password>@localhost:5432/<database_name>'
    URL_DATABASE = 'postgresql://postgres:postgres@localhost:5432/bakery'


settings = Settings()
log = BFALogger(name="BFALogger")
   