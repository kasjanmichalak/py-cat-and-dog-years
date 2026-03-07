from app.main import get_human_age


def test_for_cats_under_15() -> None:
    assert get_human_age(0, 0)[0] == 0
    assert get_human_age(14, 0)[0] == 0


def test_for_cats_between_15_and_23() -> None:
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(23, 0)[0] == 1


def test_for_cats_over_23() -> None:
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(25, 0)[0] == 2
    assert get_human_age(26, 0)[0] == 2
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3


def test_for_dogs_under_15() -> None:
    assert get_human_age(0, 0)[1] == 0
    assert get_human_age(0, 14)[1] == 0


def test_for_dogs_between_15_and_23() -> None:
    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 23)[1] == 1


def test_for_dogs_over_23() -> None:
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 25)[1] == 2
    assert get_human_age(0, 26)[1] == 2
    assert get_human_age(0, 27)[1] == 2
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3


def test_for_cats_and_dogs_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_for_cats_and_dogs_boundary_28() -> None:
    assert get_human_age(28, 28) == [3, 2]
