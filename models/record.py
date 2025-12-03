import enum

from sqlalchemy import Column, Integer, String, Date, Enum
from . import Base


class ChecksumStatusEnum(enum.Enum):
    Unknown = 0
    Verified = 1
    NotApplicable = 2
    Mismatch = 3
    NotInArchive = 4


class Record(Base):
    __tablename__ = 'records'

    row_id = Column(Integer, primary_key=True)
    organisation_id = Column(String(255))
    local_id = Column(String(255))
    md5_checksum = Column(String(32))
    md5_checksum_partner = Column(String(32), nullable=True)
    checksum_sync_status = Column(Enum(ChecksumStatusEnum), default=ChecksumStatusEnum.Unknown)
    created_at = Date()
    modified_at = Date()

    def __repr_(self):
        return f"<Record(row_id={self.row_id})>"
