from weapon import Weapon

def test_weapon_creation():
    sword = Weapon("Sword", 10)
    assert sword.name == "Sword"
    assert sword.damage == 10

def test_weapon_get_damage():
    sword = Weapon("Sword", 10)
    assert sword.get_damage() == 10
