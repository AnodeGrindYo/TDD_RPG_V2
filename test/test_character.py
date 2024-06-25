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