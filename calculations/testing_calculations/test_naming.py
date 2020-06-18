from calculations.naming import csv_name_giver, standard_number, dataframe_from_csv, rest, wikkel


def test_csv_name_giver():
    naming = csv_name_giver()
    test1 = naming("mike", 1, ".mike")
    expected = "mike_1.mike"
    assert test1 == expected


def test_standard_number():
    expected = "000001"
    expected1 = "a0001b"
    nummer = standard_number()
    test_nummer = nummer(1,0,6,"","")
    test_nummer1 = nummer(1,0,4,"a","b")

    assert test_nummer == expected
    assert test_nummer1 == expected1


def test_rest():
    expected = 0
    testrest = rest()
    extra_rollen = testrest(4, 1000, 250)
    assert extra_rollen == expected


def test_wikkel():
    wik = wikkel()
    test = wik(1000,80,76)
    expected = 7
    assert test == expected


