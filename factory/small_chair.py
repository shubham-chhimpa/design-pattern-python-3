from factory.chair import Chair
from factory.i_chair import IChair


class SmallChair(Chair, IChair):

    def __init__(self) -> None:
        """
            Small Chair Concrete class implements IChair Interface
        """
        self._height = 30
        self._width = 30
        self._depth = 30

    def get_dimension(self) -> dict:
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
