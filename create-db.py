
from database import SessionLocal
from models.record import Record

DBSession = SessionLocal()

DBSession.query(Record).delete()


DBSession.add(Record(row_id=1, organisation_id="org1", local_id="/file", md5_checksum="0284bb853a649751efbca489e6132b12", md5_checksum_partner="0284bb853a649751efbca489e6132b12"))
DBSession.add(Record(row_id=2, organisation_id="org1", local_id="/file", md5_checksum="valid_checksum", md5_checksum_partner="valid_checksum"))
DBSession.add(Record(row_id=3, organisation_id="org2", local_id="/missing_partner_checksum", md5_checksum="efg", md5_checksum_partner=None))
DBSession.add(Record(row_id=4, organisation_id="org2", local_id="/missing_partner_checksum2", md5_checksum="efg", md5_checksum_partner=None))
DBSession.add(Record(row_id=5, organisation_id="NotAPartner1", local_id="/not_a_partner", md5_checksum="valid_checksum", md5_checksum_partner="valid_checksum"))
DBSession.add(Record(row_id=6, organisation_id="org4", local_id="/hash_not_in_mediahaven", md5_checksum="hash_not_in_mediahaven", md5_checksum_partner="hash_not_in_mediahaven"))

DBSession.commit()
