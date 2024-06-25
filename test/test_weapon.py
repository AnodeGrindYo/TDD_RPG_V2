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

def test_weapon_upgrade():
    sword = Weapon("Sword", 10)
    sword.upgrade(5)
    assert sword.get_damage() == 15

def test_weapon_downgrade():
    sword = Weapon("Sword", 10)
    sword.downgrade(5)
    assert sword.get_damage() == 5
    sword.downgrade(10)
    assert sword.get_damage() == 0

def test_weapon_rename():
    sword = Weapon("Sword", 10)
    sword.rename("Excalibur")
    assert sword.name == "Excalibur"
    assert sword.describe() == "Weapon: Excalibur, Damage: 10"

def test_weapon_is_broken():
    sword = Weapon("Sword", 10)
    assert not sword.is_broken()
    sword.downgrade(10)
    assert sword.is_broken()

def test_weapon_repair():
    sword = Weapon("Sword", 10)
    sword.downgrade(10)
    assert sword.is_broken()
    sword.repair(5)
    assert sword.get_damage() == 5
    assert not sword.is_broken()

def test_weapon_enhance():
    sword = Weapon("Sword", 10)
    sword.enhance(1.5)
    assert sword.get_damage() == 15

