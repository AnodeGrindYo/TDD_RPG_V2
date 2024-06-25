from character import Character

def test_character_name():
    c = Character("Albert")
    assert c.name == "Albert"
