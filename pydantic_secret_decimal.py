from __future__ import annotations

import warnings
from decimal import Decimal
from typing import TYPE_CHECKING, Any
from typing import Dict
import pydantic

# from pydantic.v1.utils import update_not_none
from pydantic.types import _SecretField, _secret_display

# from pydantic.v1.validators import decimal_validator
# from pydantic_core import CoreSchema
# from pydantic import GetJsonSchemaHandler



if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class SecretDecimal(_SecretField[Decimal]):
    # @classmethod
    # def __get_pydantic_json_schema__(
    #     cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    # ) -> Dict[str, Any]:
    #     # json_schema = super().__get_pydantic_json_schema__(core_schema, handler)
    #     # json_schema = handler.resolve_ref_schema(json_schema)
    #     # json_schema.update(examples='examples')
    #     # return json_schema
    #     update_not_none(core_schema, type="Decimal", writeOnly=True, format="password")

    # @classmethod
    # def __get_validators__(cls) -> CallableGenerator:
    #     yield cls.validate

    # @classmethod
    # def validate(cls, value: Any) -> SecretDecimal:
    #     if isinstance(value, cls):
    #         return value
    #     value = decimal_validator(value)
    #     return cls(value)

    # def __init__(self, value: Decimal):
    #     self._secret_value = value

    # def __repr__(self) -> str:
    #     return f"SecretDecimal('{self}')"

    # def __str__(self) -> str:
    #     return "**********" if self._secret_value else ""

    # def __eq__(self, other: Any) -> bool:
    #     return (
    #         isinstance(other, SecretDecimal)
    #         and self.get_secret_value() == other.get_secret_value()
    #     )

    # def display(self) -> str:
    #     warnings.warn(
    #         "`pydantic_secret_decimal.display()` is deprecated, use `str(secret_decimal)` instead",
    #         DeprecationWarning,
    #         stacklevel=2,
    #     )
    #     return str(self)
    def _display(self) -> Decimal:
        return _secret_display(self.get_secret_value())

    # def get_secret_value(self) -> Decimal:
    #     return self._secret_value
