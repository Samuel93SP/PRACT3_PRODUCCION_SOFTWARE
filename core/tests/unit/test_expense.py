import pytest
from datetime import date
from datetime import timedelta
from core.domain_error import InvalidAmountError, InvalidExpenseDateError
from core.expense import Expense
from core.domain_error import (
    EmptyTitleError,
)


def test_create_valid_expense():
    expense = Expense(
        id=1,
        title="Comida",
        amount=10.5,
        description="Almuerzo",
        expense_date=date.today(),
    )

    assert expense.title == "Comida"
    assert expense.amount == 10.5


def test_empty_title_raises_error():
    with pytest.raises(EmptyTitleError):
        Expense(id=1, title="", amount=10, description="", expense_date=date.today())


def test_negative_amount_raises_error():
    with pytest.raises(InvalidAmountError):
        Expense(
            id=1,
            title="Gasto inválido",
            amount=-5,
            description="Negativo",
            expense_date=date.today(),
        )


def test_future_date_raises_error():
    future_day = date.today() + timedelta(days=1)
    with pytest.raises(InvalidExpenseDateError):
        Expense(
            id=1,
            title="Gasto futuro",
            amount=10,
            description="No permitido",
            expense_date=future_day,
        )
