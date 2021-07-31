from factory.chair import Chair
from factory.chair_factory import ChairFactory, ChairType

if __name__ == '__main__':
    chair: Chair = ChairFactory.get_chair(ChairType.BIG)
    print(chair.get_dimension())
