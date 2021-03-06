import pytest
from models.expense import Expense


@pytest.fixture
def ex1():
    expense = Expense("KFC", "2001-01-01", "Food", 10.56)
    return expense


def test_expense():
    expense1 = Expense("KFC", "2001-01-01", "Food", 10.56)

    assert expense1.name == "KFC"
    assert expense1.date == "2001-01-01"
    assert expense1.category == "Food"
    assert expense1.amount == 10.56


def test_invalid_expense():
    with pytest.raises(TypeError):
        Expense(100, "2001-01-01", "Food", 10.56)
    with pytest.raises(TypeError):
        Expense("KFC", 2001, "Food", 10.56)
    with pytest.raises(TypeError):
        Expense("KFC", "2001-01-01", 123, 10.56)
    with pytest.raises(TypeError):
        Expense("KFC", "2001-01-01", "Food", "0.56")

    with pytest.raises(ValueError):
        Expense("KFC", "2001-01-01", "Some Category", 10.56)
    with pytest.raises(ValueError):
        Expense("KFC", "2001-01-01", "Food", -10.56)


def test_edit_attr(ex1):
    ex1.edit_attr("name", "Movie")
    assert ex1.name == "Movie"

    ex1.edit_attr("date", "2001-11-01")
    assert ex1.date == "2001-11-01"

    ex1.edit_attr("category", "Entertainment")
    assert ex1.category == "Entertainment"

    ex1.edit_attr("amount", 12.35)
    assert ex1.amount == 12.35


def test_invalid_edit_attr(ex1):
    with pytest.raises(ValueError):
        ex1.edit_attr("amount", "12.35")


def test_get_expense_id(ex1):
    assert ex1.get_expense_id() == 4

    ex2 = Expense("KFC", "2001-02-01", "Food", 10.56)
    assert ex2.get_expense_id() == 5


def test_to_dict(ex1):
    expense1_dict = {
        "name": "KFC",
        "date": "2001-01-01",
        "category": "Food",
        "amount": 10.56,
    }

    assert ex1.to_dict() == expense1_dict
