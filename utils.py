from datetime import datetime

def validate_date(date_str):
    """Validate date string to be in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    """Validate that the amount is a positive float."""
    try:
        amount = float(amount_str)
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return True
    except ValueError:
        return False

