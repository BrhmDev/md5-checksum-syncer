from database import SessionLocal
from repository.record_repository import RecordRepository
from service.checksum_service import ChecksumService
from Scheduler import schedule_interval
from service.mediahaven_service import MediaHavenService
from service.meemoo_organisation_service import MeemooOrganisationService

def sync_checksums_task():
    DBSession = SessionLocal()

    try:
        checksumService = ChecksumService(
            RecordRepository(DBSession),
            MeemooOrganisationService(),
            MediaHavenService(),
        )
        checksumService.sync_checksums()
        DBSession.commit()
    except Exception as e:
        DBSession.rollback()
        raise e
    finally:
        DBSession.close()


schedule_interval(sync_checksums_task, 20)
