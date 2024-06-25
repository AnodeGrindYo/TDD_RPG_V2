from weapon import Weapon

def test_weapon_creation():
    sword = Weapon("Sword", 10)
    assert sword.name == "Sword"
    assert sword.damage == 10

def test_weapon_get_damage():
    sword = Weapon("Sword", 10)
    assert sword.get_damage() == 10

def test_weapon_set_damage():
    sword = Weapon("Sword", 10)
    sword.set_damage(15)
    assert sword.get_damage() == 15

def test_weapon_describe():
    sword = Weapon("Sword", 10)
    description = sword.describe()
    assert description == "Weapon: Sword, Damage: 10"
