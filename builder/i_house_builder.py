from abc import ABCMeta, abstractmethod

from builder.house import HouseType, House


class IHouseBuilder(metaclass=ABCMeta):
    @abstractmethod
    def set_house_type(self, house_type: HouseType) -> None:
        pass

    @abstractmethod
    def set_number_windows(self, number_windows: int) -> None:
        pass

    @abstractmethod
    def set_num_doors(self, number_doors: int) -> None:
        pass

    @abstractmethod
    def build(self) -> House:
        pass
