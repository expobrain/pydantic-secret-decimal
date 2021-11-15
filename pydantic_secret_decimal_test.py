from decimal import Decimal

import pytest
from pydantic import BaseModel, ValidationError

from pydantic_secret_decimal import SecretDecimal


def test_secretdecimal() -> None:
    class Foobar(BaseModel):
        value: SecretDecimal

    # Initialize the model.
    f = Foobar(value=Decimal("10"))

    # Assert correct types.
    assert f.value.__class__.__name__ == "SecretDecimal"

    # Assert str and repr are correct.
    assert str(f.value) == "**********"
    assert repr(f.value) == "SecretDecimal('**********')"

    # Assert retrieval of secret value is correct
    assert f.value.get_secret_value() == Decimal("10")

    with pytest.warns(
        DeprecationWarning, match=r"`pydantic_secret_decimal.display\(\)` is deprecated"
    ):
        assert f.value.display() == "**********"

    # Assert that SecretDecimal is equal to SecretDecimal if the secret is the same.
    assert f == f.copy()
    assert f != f.copy(update=dict(value=Decimal("20")))


def test_secretdecimal_equality() -> None:
    assert SecretDecimal(Decimal("10")) == SecretDecimal(Decimal("10"))
    assert SecretDecimal(Decimal("10")) != SecretDecimal(Decimal("20"))
    assert SecretDecimal(Decimal("10")) != Decimal("10")
    assert SecretDecimal(Decimal("10")) is not SecretDecimal(Decimal("10"))


def test_secretdecimal_idempotent() -> None:
    class Foobar(BaseModel):
        value: SecretDecimal

    # Should not raise an exception
    m = Foobar(value=SecretDecimal(Decimal("10")))
    assert m.value.get_secret_value() == Decimal("10")


def test_secretdecimal_error() -> None:
    class Foobar(BaseModel):
        value: SecretDecimal

    with pytest.raises(ValidationError) as exc_info:
        Foobar(value=[6, 23, "abc"])
    assert exc_info.value.errors() == [
        {"loc": ("value",), "msg": "value is not a valid decimal", "type": "type_error.decimal"}
    ]
