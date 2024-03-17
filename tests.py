import pytest


@pytest.mark.parametrize("str_1, str_2, strs_concatenation", [
    ("ab", "cd", "abcd"),
    ("", "abc", "abc"),
    ("\\", "n", "\\n"),
])
def test_str_concatenation(str_1, str_2, strs_concatenation):
    assert str_1 + str_2 == strs_concatenation


def test_str_get_char_from_empty():
    string = ""
    try:
        string[0]
        assert False
    except IndexError:
        pass
    assert True


def test_str_get_slice():
    string = "This is test text"
    assert string[5:7] == "is"


@pytest.mark.parametrize("tpl_1, tpl_2, tpls_concatenation", [
    ((1, 2), (3, 4), (1, 2, 3, 4)),
    (tuple(), (1, 2), (1, 2)),
])
def test_tuple_concatenation(tpl_1, tpl_2, tpls_concatenation):
    assert tpl_1 + tpl_2 == tpls_concatenation


def test_tuple_no_item_assignment():
    tpl = (1, 2, 3, "4", "5")
    try:
        tpl[0] = 10
        assert False
    except TypeError:
        pass
    assert True


def test_tuple_get_hash():
    tpl = (1, 2, 3, "4", "5")
    hash(tpl)
    assert True
