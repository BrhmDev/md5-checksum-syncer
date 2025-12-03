from models.record import Record

class MediaHavenService:
    def get_by_md5_checksum(self, records: list[Record]) -> set[int]:
        # query mediahaven with list of md5 hashes, return the row_id's

        hashes_not_in_archive = {"hash_not_in_mediahaven", "hash_not_in_mediahaven2"}

        with_found_hash = filter(lambda r: r.md5_checksum not in hashes_not_in_archive, records)
        return set([record.row_id for record in with_found_hash])

