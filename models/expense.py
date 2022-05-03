import itertools

CATEGORIES = [
    "Food",
    "Apparel",
    "Entertainment",
    "Lifestyle",
    "Miscellaneious",
    "Groceries",
    "Services",
    "Technology",
    "School",
]


class Expense:

    id_iter = itertools.count(start=1, step=1)

    def __init__(self, name, date, category, amount):
        if type(name) is not str:
            raise TypeError

        # format: MM/DD/YYYY, done in HTML
        if type(date) is not str:
            raise TypeError

        if len(date) != 10:
            raise ValueError

        if (
            (date[0:2].isnumeric() == False)
            or (date[3:5].isnumeric() == False)
            or (date[6:10].isnumeric() == False)
        ):
            raise ValueError

        if date[2] != "/" or date[5] != "/":
            raise ValueError

        if type(category) is not str:
            raise TypeError

        if category not in CATEGORIES:
            raise ValueError

        if type(amount) is not int and type(amount) is not float:
            raise TypeError

        if amount < 0:
            raise ValueError

        self.id = next(Expense.id_iter)
        self.name = name
        self.date = date
        self.category = category
        self.amount = amount

    def edit_attr(self, attr: str, value):
        """Edit an expense attribute"""
        if attr == "name":
            self.name = value

        if attr == "date":
            self.date = value

        if attr == "category":
            self.category = value

        if attr == "amount":
            if type(value) not in [int, float]:
                raise ValueError

            self.amount = value

    def get_expense_id(self):
        return self.id

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
        }
