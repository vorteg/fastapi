# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
#                            backref)
"""
SQLite Models. Database 1
"""
engine = create_engine('sqlite:///database.sqlite3',
                       convert_unicode=True,
                       echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

data = ({
    "Id": 1,
    "Name": "Audi",
    "Price": 52642
}, {
    "Id": 2,
    "Name": "Mercedes",
    "Price": 57127
}, {
    "Id": 3,
    "Name": "Skoda",
    "Price": 9000
}, {
    "Id": 4,
    "Name": "Volvo",
    "Price": 29000
}, {
    "Id": 5,
    "Name": "Bentley",
    "Price": 350000
}, {
    "Id": 6,
    "Name": "Citroen",
    "Price": 21000
}, {
    "Id": 7,
    "Name": "Hummer",
    "Price": 41400
}, {
    "Id": 8,
    "Name": "Volkswagen",
    "Price": 21600
})


class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand_id = Column(String)
    year = Column(Integer)


def get_model(info, id):
    from schema import Model as ModelSchema
    model = ModelSchema.get_query(info)
    return [f for f in model.filter_by(brand_id=id)]
