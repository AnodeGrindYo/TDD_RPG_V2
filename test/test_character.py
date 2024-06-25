from character import Character

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
