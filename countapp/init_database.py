from sqlalchemy import create_engine, Column, VARCHAR, INT, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MYSQL_HOST = config('DB_HOST')
MYSQL_PORT = config('DB_PORT')
MYSQL_USER = config('DB_USER')
MYSQL_PASSWORD = config('DB_PASSWORD')
MYSQL_DB = config('DB_DATABASE')


url = 'mysql+pymysql://' + MYSQL_USER +':' + MYSQL_PASSWORD + '@' + MYSQL_HOST + ':' + MYSQL_PORT + '/' + MYSQL_DB + '?charset=utf8'
if not database_exists(url):
    create_database(url)

Base = declarative_base()
engine = create_engine(url, echo=True)

class CounterTable(Base):
    __tablename__ = 'counter'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci'
    }
    name = Column(VARCHAR(32), primary_key=True, nullable=False)
    count = Column(INT, default=None)


Base.metadata.create_all(engine,tables=[CounterTable.__table__])

Session = sessionmaker(bind=engine)
session = Session()
stmt = select(CounterTable).where(CounterTable.name == 'test')
result = session.execute(stmt).fetchone()
print(result, '//////////')
if not result:
    new_record = CounterTable(name='test', count='0')
    session.add(new_record)
    session.commit()