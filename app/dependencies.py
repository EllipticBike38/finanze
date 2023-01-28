from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def get_db():
    try:
        db = Session()
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
