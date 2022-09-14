from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, Date
import json


# Connect to Postgresql
engine = create_engine('postgresql://postgres:1111@localhost:5433/selenium_test')
Base = declarative_base(engine)

# Model for DB.
class Ad(Base):
    __tablename__ = 'Ads'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    title = Column(String)
    date = Column(Date)
    city = Column(String)
    beds = Column(String)
    text = Column(String)
    price = Column(String)
    currency = Column(String)


# This function can create DB.
def create_db():
    Base.metadata.create_all()


# This function saves data in DB.
def save_to_db(data):
    for i in range(len(data)):
        new_data = Ad(image=data[i]['image'], title=data[i]['title'], date=data[i]['date'],
                      city=data[i]['city'], beds=data[i]['beds'], text=data[i]['description'],
                      price=data[i]['price'], currency=data[i]['currency'])
        session = Session(engine)
        session.add(new_data)
        session.commit()

    return 1

# This function get data from DB.
def get_from_db():
    session = Session(engine)
    elements = session.query(Ad).all()
    print(len(elements))
    data = []
    for el in elements:
        print(el.title, '  ', el.date)
        data.append({'title': el.title, 'image': el.image,
                     'date': str(el.date), 'city': el.city,
                     'beds': el.beds, 'price': el.price,
                     'description': el.text, 'currency': el.currency
                     })
    with open('sample.json', 'w') as f:  # All data I saved in json file.
        json.dump(data, f)
    return elements
