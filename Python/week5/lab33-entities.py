


class Entity:
    def __init__(self, name, symbol, loc_i, loc_j):
        self.name = name
        self.symbol = symbol
        self.loc_i = loc_i
        self.loc_j = loc_j


class LivingEntity(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, health, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.health = health
        self.attack = attack
        self.defense = defense


class Player(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Player', '☻')





