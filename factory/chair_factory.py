from enum import Enum

from factory.big_chair import BigChair
from factory.chair import Chair
from factory.small_chair import SmallChair


class ChairType(Enum):
    SMALL = 0
    BIG = 1


class ChairFactory:
    """
        Chair Factory Class
    """

    @staticmethod
    def get_chair(chair_type: ChairType) -> Chair:
        """
        :param chair_type:
        :return: Chair:Chair Class Object
        """
        if chair_type == ChairType.BIG:
            return BigChair()
        if chair_type == ChairType.SMALL:
            return SmallChair()
        else:
            raise ValueError(f"{chair_type} implementation not found")
