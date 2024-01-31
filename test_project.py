from project import check_login, check_register, chance_calculator

def test_check_login():
    assert check_login(" ", "") == False
    assert check_login("", " ") == False


def test_check_register():
    assert check_register("","") == False
    assert check_register(" asd ", "ads") == False
    assert check_register("zxc", "zxc") == False
    assert check_register("asd", "zxc") == True


def test_chance_calculator():
    assert chance_calculator(2, 4) == "50.0%"
    assert chance_calculator(1, 5) == "20.0%"
    assert chance_calculator(3, 7) == "43.0%"
    assert chance_calculator(0, 4) == "0.0%"
    assert chance_calculator(5, 11) == "45.0%"