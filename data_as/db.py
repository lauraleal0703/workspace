from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://datastudio:GYR4nka2nqt*rkv.xpg@172.16.33.8/otrs?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()