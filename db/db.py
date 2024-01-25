from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import path, sep

BASE = declarative_base() 
engine = create_engine(f'sqlite:///{path.realpath("db")+sep}entradaYSalida.db')

Session = sessionmaker(bind=engine)
session = Session()
