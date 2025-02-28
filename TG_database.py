from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://###/my_database"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Data(Base):
    __tablename__ = 'database'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

def save_data(name, surname, age):
    new_data = Data(name=name, surname=surname, age=age)
    session.add(new_data)
    session.commit()

def read_data():
    records = session.query(Data).all()
    return [f"ID: {record.id}, Имя: {record.name}, Фамилия: {record.surname}, Возраст: {record.age}" for record in records]

def delete_data(record_id):
    record = session.query(Data).filter_by(id=record_id).first()
    if record:
        session.delete(record)
        session.commit()
        return True
    return False