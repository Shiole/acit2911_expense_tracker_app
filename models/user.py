from models.expense import Expense
import hashlib


class User:
    def __init__(self, name, username, email, password):
        if (
            type(name) is not str
            or type(username) is not str
            or type(email) is not str
            or type(password) is not str
        ):
            raise TypeError

        if (
            any(chr.isdigit() for chr in password) == False
            or any(chr.isalpha() for chr in password) == False
            or len(password) < 8
            or len(username) < 5
            or "@" not in email
        ):
            raise ValueError

        self.name = name
        self.username = username
        self.email = email
        self.password = str(hashlib.sha256(password.encode()).hexdigest())

    #     self.expenses = expenses

    # def add_expense(self, expense: Expense):
    #     """Add an expense to user's list"""
    #     if type(expense) is not Expense:
    #         raise TypeError

    #     self.expenses.append(expense.to_dict())

    # def delete_expense(self, expense: Expense):
    #     """Remove an expense from user's list

    #     Note: probably not right, need to fix
    #     """
    #     index = None
    #     for i, e in enumerate(self.expenses):
    #         if e.get_expense_id() == expense.get_expense_id():
    #             index = i
    #             break

    #     del self.expenses[index]

    # def to_dict(self):
    #     expenses = [e.to_dict() for e in self.expenses]

    #     user_dict = {
    #         "name": self.name,
    #         "username": self.username,
    #         "email": self.email,
    #         "password": self.password,
    #         "expenses": expenses
    #     }

    #     return user_dict
