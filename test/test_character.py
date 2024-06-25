from character import Character, HealingItem
from weapon import Weapon

def test_character_name():
    c = Character("Albert")
    assert c.name == "Albert"

def test_character_hp_when_created():
    c = Character("Albert")
    assert c.hp == 100

def test_character_is_alive_when_created():
    c = Character("Albert")
    assert c.is_alive == True

def test_character_get_damage():
    c = Character("Albert")
    c.get_damage(10)
    assert c.hp == 90

def test_character_get_damage_negative():
    c = Character("Albert")
    try:
        c.get_damage(-10)
    except ValueError as e:
        assert str(e) == "damage should be positive"

def test_character_hp_not_negative():
    c = Character("Albert")
    c.get_damage(110)
    assert c.hp == 0

def test_character_is_dead_when_hp_is_zero():
    c = Character("Albert")
    c.get_damage(100)
    assert c.hp == 0
    assert c.is_alive == False

def test_character_heal():
    c = Character("Albert")
    c.get_damage(50)
    c.heal(30)
    assert c.hp == 80

def test_character_heal_cannot_exceed_max_hp():
    c = Character("Albert")
    c.get_damage(10)
    c.heal(20)
    assert c.hp == 100

def test_character_heal_negative():
    c = Character("Albert")
    try:
        c.heal(-10)
    except ValueError as e:
        assert str(e) == "heal amount should be positive"

def test_character_drinks_potion():
    c = Character("Albert")
    c.get_damage(50)
    c.drink_potion(HealingItem.POTION)
    assert c.hp == 75

def test_character_drinks_super_potion():
    c = Character("Albert")
    c.get_damage(50)
    c.drink_potion(HealingItem.SUPER_POTION)
    assert c.hp == 100

def test_character_drinks_hyper_potion():
    c = Character("Albert")
    c.get_damage(50)
    c.drink_potion(HealingItem.HYPER_POTION)
    assert c.hp == 100

def test_character_drinks_invalid_potion():
    c = Character("Albert")
    try:
        c.drink_potion("INVALID_POTION")
    except ValueError as e:
        assert str(e) == "Invalid potion type"

def test_put_potion_into_inventory_valid():
    c = Character("Albert")
    c.put_potion_into_inventory(HealingItem.POTION)
    assert HealingItem.POTION in c.inventory

def test_put_potion_into_inventory_invalid():
    c = Character("Albert")
    try:
        c.put_potion_into_inventory("INVALID_POTION")
    except ValueError as e:
        assert str(e) == "Invalid potion type"

def test_put_potion_into_inventory_full():
    c = Character("Albert")
    for _ in range(5):
        c.put_potion_into_inventory(HealingItem.POTION)
    try:
        c.put_potion_into_inventory(HealingItem.SUPER_POTION)
    except ValueError as e:
        assert str(e) == "Inventory is full"

def test_remove_potion_from_inventory():
    c = Character("Albert")
    c.put_potion_into_inventory(HealingItem.POTION)
    c.remove_potion_from_inventory(HealingItem.POTION)
    assert HealingItem.POTION not in c.inventory

def test_use_potion_from_inventory():
    c = Character("Albert")
    c.put_potion_into_inventory(HealingItem.POTION)
    c.get_damage(50)
    c.use_potion_from_inventory(HealingItem.POTION)
    assert c.hp == 75
    assert HealingItem.POTION not in c.inventory

def test_character_deal_damage():
    c1 = Character("Albert")
    c2 = Character("Bob")
    c1.deal_damage(c2, 10)
    assert c2.hp == 90

def test_is_inventory_full():
    c = Character("Albert")
    for _ in range(5):
        c.put_potion_into_inventory(HealingItem.POTION)
    assert c.is_inventory_full()


def test_character_deal_damage_and_heal():
    c1 = Character("Alice")
    c2 = Character("Bob")
    c1.deal_damage(c2, 30)
    assert c2.hp == 70
    c2.heal(20)
    assert c2.hp == 90

def test_equip_weapon():
    c = Character("Albert")
    sword = Weapon("Sword", 10)
    c.equip_weapon(sword)
    assert c.weapon == sword
