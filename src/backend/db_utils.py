"""module with some helping stuff for db"""
from typing import Optional

import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DBStuff:
    def __init__(self) -> None:
        self._sqlalchemy_url = "postgresql+pg8000:"+\
        "//postgres:hackme@0.0.0.0/postgres"
        self._db_engine: Engine = create_engine(
            self._sqlalchemy_url, echo=True
        )

    def create_session(self) -> Session:
        return Session(self._db_engine)

    @property
    def sqlalchemy_url(self) -> str:
        return self._sqlalchemy_url
