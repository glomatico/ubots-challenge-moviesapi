from sqlmodel import SQLModel, create_engine

from .constants import URL_DATABASE

engine = create_engine(URL_DATABASE)


def create_database():
    SQLModel.metadata.create_all(engine)
