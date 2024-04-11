from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    __tablename__ = "todos"

    id = Column(
        Integer, primary_key=True, index=True
    )  # index means unique; increase the id???
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False) # 0 = False, 1 = True in a Database
