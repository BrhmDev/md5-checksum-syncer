import datetime
import enum

from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from . import Base


class ChecksumStatusEnum(enum.Enum):
    Unknown = 0
    Verified = 1
    NotApplicable = 2
    NotInArchive = 3


class Record(Base):
    __tablename__ = 'records'

    row_id = Column(Integer, primary_key=True)
    organisation_id = Column(String(255))
    local_id = Column(String(255))
    md5_checksum = Column(String(32), nullable=True)
    checksum_sync_status = Column(Enum(ChecksumStatusEnum), default=ChecksumStatusEnum.Unknown)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Record(row_id={self.row_id}, organisation_id={self.organisation_id}, local_id={self.local_id}, md5_checksum={self.md5_checksum}, checksum_sync_status={self.checksum_sync_status})>"
