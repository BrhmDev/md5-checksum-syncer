from repository.record_repository_protocol import RecordRepositoryProtocol
from models.record import ChecksumStatusEnum, Record


class ChecksumService:
    def __init__(self, record_repository: RecordRepositoryProtocol, organisation_service, archival_service, notification_service):
        self.record_repository = record_repository
        self.organisation_service = organisation_service
        self.archival_service = archival_service
        self.notification_service = notification_service

    def sync_checksums(self):
        records_to_sync = self.record_repository.get_ready_to_sync()

        matched_org_ids = set([record.organisation_id for record in records_to_sync])
        partner_ids: set[int] = self.organisation_service.get_partners_by_ids(matched_org_ids)

        partner_records: list[Record] = []
        for record in records_to_sync:
            if record.organisation_id not in partner_ids:
                record.checksum_sync_status = ChecksumStatusEnum.NotApplicable
            else:
                partner_records.append(record)

        found_hash_ids: set[int] = self.archival_service.get_by_md5_checksum(partner_records)
        for record in partner_records:
            if record.row_id in found_hash_ids:
                record.checksum_sync_status = ChecksumStatusEnum.Verified
            else:
                record.checksum_sync_status = ChecksumStatusEnum.NotInArchive
                self.notification_service.send_partner_notification(
                    record.organisation_id, "Warning",
                    F"Record with id: {record.local_id} checksum provided by partner cannot be found in archive."
                )
