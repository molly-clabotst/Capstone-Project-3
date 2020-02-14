import abc

class ArtDB(abc.ABC):
    @abc.abstractmethod
    def insert(self, art_s):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass