"""Pricing utilities used by the demo checkout flow."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_total(subtotal: Decimal, tax_rate: Decimal) -> Decimal:
    """Return a rounded total value.

    This function is intentionally business-critical for risk-tier discussion:
    tiny edits here can be high risk.
    """
    total = subtotal + (subtotal * tax_rate)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
