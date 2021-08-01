from builder.house import HouseType, House
from builder.i_house_builder import IHouseBuilder


class HouseBuilder(IHouseBuilder):

    def __init__(self):
        self._house = House()

    def set_house_type(self, house_type: HouseType) -> 'HouseBuilder':
        self._house.house_type = house_type
        return self

    def set_number_windows(self, number_windows: int) -> 'HouseBuilder':
        self._house.number_windows = number_windows
        return self

    def set_num_doors(self, number_doors: int) -> 'HouseBuilder':
        self._house.number_doors = number_doors
        return self

    def build(self) -> House:
        return self._house
