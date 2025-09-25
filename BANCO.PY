from sqlalchemy import create_engine

from sqlalchemy.orm import declaretive_base, sessionmake
 
DATABASE_URL= 'sqlite:///relacoes.db' \
 
engine=create_engine(DATABASE_URL  , echo=False , future=True)