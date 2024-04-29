import datetime
from application import salary
from application.db import people

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(datetime.date.today())
    salary.salary_func(123)
    people.add_people("Денис")