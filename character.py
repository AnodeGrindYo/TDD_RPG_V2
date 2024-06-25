from enum import Enum

class HealingItem(Enum):
    POTION = 25
    SUPER_POTION = 50
    HYPER_POTION = 100

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.is_alive = True
        self.inventory = []
        self.max_inventory_size = 5

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

    def drink_potion(self, potion):
        if potion not in HealingItem:
            raise ValueError("Invalid potion type")
        self.heal(potion.value)

    def put_potion_into_inventory(self, potion):
        if type(potion) != HealingItem:
            raise ValueError("Invalid potion type")
        if len(self.inventory) >= self.max_inventory_size:
            raise ValueError("Inventory is full")
        self.inventory.append(potion)

    def remove_potion_from_inventory(self, potion):
        if potion not in self.inventory:
            raise ValueError("Potion not in inventory")
        self.inventory.remove(potion)   

    def use_potion_from_inventory(self, potion):
        if potion in self.inventory:
            self.drink_potion(potion)
            self.inventory.remove(potion)
        else:
            raise ValueError("Potion not in inventory") 
    
    def deal_damage(self, character, damage):
        character.get_damage(damage)   

    def is_inventory_full(self):
        return len(self.inventory) >= self.max_inventory_size
    
    
    
