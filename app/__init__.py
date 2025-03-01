from fastapi import FastAPI

from app.models.base_model import Base
from app.models.db_session import engine


class AppFactory:
    @classmethod
    def init_tables(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def create_app(cls):
        try:
            app = FastAPI(title="EMA")

            cls.init_tables()
            return app

        except Exception as e:
            print("exception occurred in create_app", str(e))
