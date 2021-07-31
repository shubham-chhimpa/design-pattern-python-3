from factory.chair import Chair
from factory.i_chair import IChair


class BigChair(Chair, IChair):
    """
            Big Chair Concrete class implements IChair Interface
    """

    def __init__(self) -> None:
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimension(self) -> dict:
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
