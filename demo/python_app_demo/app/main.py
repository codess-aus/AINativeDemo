"""Small runnable entrypoint for the demo app."""

from decimal import Decimal

from demo.python_app_demo.app.logging_utils import get_logger
from demo.python_app_demo.app.pricing import calculate_total


def run_demo() -> str:
    logger = get_logger("demo.checkout")
    subtotal = Decimal("19.99")
    tax_rate = Decimal("0.10")
    total = calculate_total(subtotal, tax_rate)
    logger.info("Calculated total for checkout flow")
    return f"Checkout total: {total}"


if __name__ == "__main__":
    print(run_demo())
