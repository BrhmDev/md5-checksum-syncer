from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from models.record import Record

engine = create_engine('sqlite:///records.sqlite', echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
