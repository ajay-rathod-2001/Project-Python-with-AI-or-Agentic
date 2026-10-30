
"""
Data Models for Expense Tracking
"""

from dataclasses import dataclass

@dataclass

class Transaction:
    date: str
    merchant: str
    amount: float
    category : str = "Uncategorized"

@dataclass
class ExpenseSummary:
    total_spent: float
    category_totals: dict[str, float]
    is_over_budget: bool
