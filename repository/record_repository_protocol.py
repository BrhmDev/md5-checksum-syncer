from typing import Protocol
from models.record import Record



class RecordRepositoryProtocol(Protocol):
    def get_ready_to_sync(self) -> list[Record]:
        ...
