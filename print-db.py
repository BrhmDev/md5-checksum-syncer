from database import SessionLocal
from models.record import Record

DBSession = SessionLocal()

records = DBSession.query(Record).all()
print("\nRecords table:")
for record in records:
    print(record)
