from enum import Enum


class HouseType(Enum):
    MUD = "mud"
    WOOD = "wood"
    CONCRETE = "concrete"


class House:
    """
        House Class
    """

    def __init__(self, house_type: HouseType = HouseType.CONCRETE, number_windows: int = 0, number_doors: int = 0):
        self.house_type = house_type
        self.number_windows = number_windows
        self.number_doors = number_doors

    def construct(self):
        print(f"{self.house_type.value} house with {self.number_windows} windows and {self.number_doors} doors")
