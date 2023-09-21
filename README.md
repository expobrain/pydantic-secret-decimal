# pydantic-secret-decimal

[![Unit testing, formatting & linting](https://github.com/expobrain/pydantic-secret-decimal/actions/workflows/main.yml/badge.svg)](https://github.com/expobrain/pydantic-secret-decimal/actions/workflows/main.yml)

This package provides a Pydantic field `SecretDecimal` to store Decimal types as secret the same as the Pydantic's standard `SecretStr` and `SecretBytes` fields (see the [official docs](https://pydantic-docs.helpmanual.io/usage/types/#secret-types)).

An use case for the `SecretDecimal` is when storing latitude and longitude of an user which is considered as PII.
