from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

class Car(object):
    pass


def loadSession(db):
    engine = create_engine(f'sqlite:///{db}', echo=True)
    metadata = MetaData(engine)
    car_params = Table('cars', metadata, autoload  = True)

    print(type(car_params), car_params.unique_params)

    mapper(Car,car_params)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    db = 'orm.sqlite'
    session = loadSession(db)
   # cars_query = session.query(Car).all()

    # filter
    cars_query = session.query(Car).filter(Car.model.in_(['Volvo','BMW'] )).all()


    for car in cars_query:
        print(car.model)