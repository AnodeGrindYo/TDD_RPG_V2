from character import Character

def test_character_name():
    c = Character("Albert")
    assert c.name == "Albert"

def test_character_hp():
    c = Character("Albert")
    assert c.hp == 100