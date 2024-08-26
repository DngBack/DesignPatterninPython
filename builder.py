# Product
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.doors} doors, {self.windows} windows, and {self.roof} roof."


# Builder
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def get_house(self):
        return self.house


# Director
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls("brick").build_doors("wooden").build_windows("glass").build_roof("tiles")
        return self.builder.get_house()


# Client
builder = HouseBuilder()
director = HouseDirector(builder)
house = director.construct_house()
print(house)