class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.is_alive = True

    def get_damage(self, damage):
        if damage < 0:
            raise ValueError("damage should be positive")
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        if self.hp == 0:
            self.is_alive = False

    def heal(self, amount):
        if amount < 0:
            raise ValueError("heal amount should be positive")
        self.hp += amount
        if self.hp > 100:
            self.hp = 100