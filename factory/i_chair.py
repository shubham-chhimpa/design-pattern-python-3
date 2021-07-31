from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """The Chair Interface"""

    @abstractmethod
    def get_dimension(self):
        """ A abstract interface method """
