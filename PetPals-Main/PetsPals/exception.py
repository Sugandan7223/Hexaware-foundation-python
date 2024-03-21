
from abc import ABC, abstractmethod


class AdoptionException(Exception):
    pass


class InvalidPetAgeException(Exception):
    pass


class FileHandlingException(Exception):
    pass


class NullReferenceException(Exception):
    pass


class DatabaseOperationException(Exception):
    pass

class IAdoptable(ABC):
    @abstractmethod
    def Adopt(self):
        pass