class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

    def describe(self):
        return f"Weapon: {self.name}, Damage: {self.damage}"

    def upgrade(self, increment):
        self.damage += increment

    def downgrade(self, decrement):
        self.damage -= decrement
        if self.damage < 0:
            self.damage = 0

    def rename(self, new_name):
        self.name = new_name

    def is_broken(self):
        return self.damage == 0

    def repair(self, amount):
        if self.damage == 0:
            self.damage = amount
