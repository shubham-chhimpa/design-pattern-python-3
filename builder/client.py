from builder.house import House, HouseType
from builder.house_builder import HouseBuilder

if __name__ == '__main__':
    house: House = HouseBuilder().set_house_type(house_type=HouseType.WOOD) \
        .set_num_doors(number_doors=5).build()
    house.construct()
