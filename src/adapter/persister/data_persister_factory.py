from adapter.persister.local_persister_adapter import LocalPersisterAdapter
from adapter.persister.data_persister import DataPersister


class DataPersisterFactory():
    @staticmethod
    def get_persister() -> DataPersister:
        return LocalPersisterAdapter()