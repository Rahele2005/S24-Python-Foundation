"""
We will create a program to track our monthly expenses.


The git will be used as a "database". For example, we will update the salary, take the output from console 
and save it in the same file.
After each function execution, manually update the value in file, commit and push to github.

Future improvement:
1) Use classes and objects. How the globle variable will be used in the class?
2) Once we learn file i/o or some api or database, we will replace the manual steps
"""

bank_balance = 3000
salary = 3000
salary_drawn_count = 1
expenses = [
    "rent",
    "food",
    "clothes",
    "travel",
    "other"
]

# write a function to add salary to bank balance only if it's first of the month. also update salaris drawn count
def salary_arrived():
    # your code here

    print("bank balance: ", bank_balance)


salary_arrived()


# write a function to add bonus to the bank balance. take the ammount from user. can you think of any edge case?
def add_bonus():
    # your code here

    print("bank balance after bonus: ", bank_balance)


add_bonus()


# write a function to add expenses. ask user for each type of expense and update bank balance
def add_expenses():
    # your code here

    print("bank balance after expenses: ", bank_balance)


add_expenses()


# write a function to tell me how much i can spend per day this month
def daily_limit():
    # your code here


daily_limit()


# write a function to increae the salary by certain percentage. see how input is different from add bonus
def salary_increase(increment_percentage: float):
    # your code here

    print("new salary: ", salary)


salary_increase()


# write a funtion to add new type of expense.
def add_new_expense():
    # your code here

    print(f"Expanse list: {expenses}")

add_new_expense()


# imrovment on the add expense function. we don't want use over and over. 
def add_expense_without_user_promt(expenses: dict):
    # your code here

    print(f"Expanse list: {expenses}")

add_expense_without_user_promt({
    "rent": 1000,
})

add_expense_without_user_promt({
    "clothes": 200,
    "food": 300.0
})


# write code to ask user which operation he wants to perform and then call only that function
