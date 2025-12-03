from sqlalchemy.orm import Session
from models.record import Record, ChecksumStatusEnum


class RecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_ready_to_sync(self) -> list[Record]:
        return self.session.query(Record).filter(
            Record.md5_checksum_partner  != None,
            Record.checksum_sync_status == ChecksumStatusEnum.Unknown
        ).all()
