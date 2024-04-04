# Python Postgres Database Communication Demo

This Python application showcases communication with a Postgres database using SQLAlchemy ORM and Alembic.

## Implementation:

1. **Run Docker container**:

    ```
    docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
    ```

    For the password, use '1234'.

2. **To create DB tables**, run in the project root:

    ```
    alembic upgrade head
    ```

3. **Fill tables with data using Faker library**. For macOS, run:

    ```
    python3 seed.py
    ```

4. **To see request result**, run:

    ```
    python3 my_select.py
    ```

Upon executing the application, you will receive responses in the console corresponding to various requests:

**Response Example:**

1. **Top 5 Students with Highest Average Grade**:

    ```
    [('Andrea Long', Decimal('60')), ('Emma Cross', Decimal('59')), ('Gary Vega', Decimal('59')), ('David Cook', Decimal('57')), ('John Dixon', Decimal('57'))]
    ```

2. **Student with Highest Average Grade in Specific Subject**:

    ```
    [('Emma Cross', 'Pharmacologist', Decimal('83'))]
    ```

3. **Average Grade in Groups for Specific Subject**:

    ```
    [('North Michelle', 'Pharmacologist', Decimal('50')), ('Leeburgh', 'Pharmacologist', Decimal('49')), ('Ashleymouth', 'Pharmacologist', Decimal('44'))]
    ```

4. **Average Grade Across All Subjects**:

    ```
    [(Decimal('50'),)]
    ```

5. **Courses Taught by Specific Teacher**:

    ```
    [('Fine artist',), ('Higher education lecturer',), ('Licensed conveyancer',), ('IT technical support officer',)]
    ```

6. **List of Students in Specific Group**:

    ```
    [('Trevor Morales',), ('Mason Gardner',), ('Alexander Watson',), ('Courtney Villarreal',), ('Emma Cross',), ('Douglas Rivera',), ('Patricia Le',), ('Gary Vega',), ('Roy Thompson',), ('Catherine Riley',), ('Chase Gonzalez',), ('Deborah Medina',), ('Kendra Pittman',), ('Anthony Crawford',), ('Alan Lucas',), ('Krista Bailey',), ('Adam Kelly',), ('Casey Olson',), ('Thomas Bender',), ('Seth Rose',), ('Katelyn Mccormick DVM',), ('Madeline Shepherd',), ('Keith Perez',), ('Mary Maddox',), ('Miranda Hogan',), ('Cody Banks',), ('Michael Wang',), ('Sarah Miles',), ('David Snow',), ('William Flores',), ('Sean Meyer',), ('Jonathan Adams',), ('Makayla Torres',), ('Vanessa Walters',), ('Michelle Alexander',)]
    ```

7. **Grades of Students in Specific Group for Specific Subject**:

    ```
    [('Krista Bailey', 25, 51), ('Adam Kelly', 25, 88), ('Catherine Riley', 25, 21), ('Deborah Medina', 25, 58), ('Douglas Rivera', 25, 45), ('Deborah Medina', 25, 93), ('Roy Thompson', 25, 63), ('Emma Cross', 25, 100), ('Adam Kelly', 25, 44), ('Anthony Crawford', 25, 27), ('Deborah Medina', 25, 34), ('Catherine Riley', 25, 80), ('Anthony Crawford', 25, 87), ('Krista Bailey', 25, 36), ('Krista Bailey', 25, 9), ('Emma Cross', 25, 40), ('Gary Vega', 25, 24), ('Adam Kelly', 25, 14), ('Adam Kelly', 25, 13), ('Deborah Medina', 25, 59), ('Deborah Medina', 25, 79), ('Chase Gonzalez', 25, 5), ('Anthony Crawford', 25, 21), ('Patricia Le', 25, 53), ('Douglas Rivera', 25, 41), ('Kendra Pittman', 25, 68), ('Mason Gardner', 25, 46), ('Chase Gonzalez', 25, 71), ('Douglas Rivera', 25, 31), ('Emma Cross', 25, 92), ('Douglas Rivera', 25, 77), ('Mason Gardner', 25, 93), ('Alexander Watson', 25, 18), ('Roy Thompson', 25, 4), ('Gary Vega', 25, 70), ('Catherine Riley', 25, 66), ('Patricia Le', 25, 99), ('Mason Gardner', 25, 30), ('Adam Kelly', 25, 37), ('Chase Gonzalez', 25, 67), ('Patricia Le', 25, 23), ('Adam Kelly', 25, 48), ('Kendra Pittman', 25, 29), ('Alexander Watson', 25, 37), ('Krista Bailey', 25, 90), ('Douglas Rivera', 25, 99), ('Patricia Le', 25, 38), ('Emma Cross', 25, 98), ('Douglas Rivera', 25, 13), ('Deborah Medina', 25, 70), ('Catherine Riley', 25, 8), ('Krista Bailey', 25, 18), ('Krista Bailey', 25, 99), ('Anthony Crawford', 25, 12), ('Catherine Riley', 25, 67

), ('Alexander Watson', 25, 19), ('Deborah Medina', 25, 17), ('Catherine Riley', 25, 99), ('Krista Bailey', 25, 21), ('Kendra Pittman', 25, 59), ('Trevor Morales', 25, 45), ('Patricia Le', 25, 49), ('Mason Gardner', 25, 10)]
    ```

8. **Average Grade Given by Specific Teacher for Their Subjects**:

    ```
    [(Decimal('51'),)]
    ```

9. **List of Courses Attended by Specific Student**:

    ```
    [('Fine artist',), ('Higher education lecturer',), ('Pharmacologist',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Higher education lecturer',), ('Fine artist',), ('Financial adviser',), ('Higher education lecturer',), ('Higher education lecturer',), ('Pharmacologist',), ('Fine artist',), ('Armed forces technical officer',), ('Pharmacologist',), ('Financial adviser',), ('Armed forces technical officer',), ('Fine artist',), ('Higher education lecturer',), ('Armed forces technical officer',), ('Higher education lecturer',), ('Armed forces technical officer',), ('Financial adviser',), ('Higher education lecturer',), ('Financial adviser',), ('Financial adviser',), ('Higher education lecturer',), ('Higher education lecturer',), ('Fine artist',)]
    ```

10. **Courses Taught by Specific Teacher to Specific Student**:

    ```
    [('Armed forces technical officer',), ('Financial adviser',), ('Financial adviser',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',), ('Armed forces technical officer',)]
    ```

11. **Average Grade Given by Specific Teacher to Specific Student**:

    ```
    [(Decimal('53'),)]
    ```

12. **Grades of Students in Specific Group for Specific Subject on Last Class**:

    ```
    [('Catherine Riley', 21, datetime.datetime(2024, 1, 1, 0, 0)), ('Adam Kelly', 44, datetime.datetime(2024, 1, 1, 0, 0)), ('Anthony Crawford', 27, datetime.datetime(2024, 1, 1, 0, 0)), ('Adam Kelly', 14, datetime.datetime(2024, 1, 1, 0, 0)), ('Deborah Medina', 59, datetime.datetime(2024, 1, 1, 0, 0)), ('Kendra Pittman', 68, datetime.datetime(2024, 1, 1, 0, 0)), ('Mason Gardner', 46, datetime.datetime(2024, 1, 1, 0, 0)), ('Douglas Rivera', 31, datetime.datetime(2024, 1, 1, 0, 0)), ('Douglas Rivera', 77, datetime.datetime(2024, 1, 1, 0, 0)), ('Catherine Riley', 66, datetime.datetime(2024, 1, 1, 0, 0)), ('Mason Gardner', 30, datetime.datetime(2024, 1, 1, 0, 0)), ('Adam Kelly', 37, datetime.datetime(2024, 1, 1, 0, 0)), ('Chase Gonzalez', 67, datetime.datetime(2024, 1, 1, 0, 0)), ('Douglas Rivera', 99, datetime.datetime(2024, 1, 1, 0, 0)), ('Deborah Medina', 70, datetime.datetime(2024, 1, 1, 0, 0)), ('Krista Bailey', 18, datetime.datetime(2024, 1, 1, 0, 0)), ('Krista Bailey', 99, datetime.datetime(2024, 1, 1, 0, 0)), ('Anthony Crawford', 12, datetime.datetime(2024, 1, 1, 0, 0)), ('Krista Bailey', 21, datetime.datetime(2024, 1, 1, 0, 0)), ('Patricia Le', 49, datetime.datetime(2024, 1, 1, 0, 0))]
    ```
