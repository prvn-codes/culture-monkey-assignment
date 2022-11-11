# Culture Monkey Assignment - Praveen S

---

# Stack

The stack I have choosed for this assignment is as follows

- Python for Backend
- Flask Framework
- SQLAlchemy for Database

---

# `models.py`

The `models.py` file contains the database structure, created to tables Employee and departments as follows:

- ```
    Employee(
                id,
                first_name,
                last_name,
                email_address,
                phone,
                salary,
                dept_id
            )
    ```

- ```
    Departments(
                    id,
                    dept_name
                )
    ```

The dept_id is a foreign key to the objects in the Departments table.

The database is populated with some default values everytime the home page is loaded.

---

# `app.py`

The `app.py` contains the framework and routing for the webapp. 

There are 2 pages:
- Home page
- Assignment page

Home page is just to give a intro page and the assignment is executed in the assignment page.

# How to run?

- Clone this repository to your local machine.
- Open terminal in the project directory
- Recommended : 
    - Create a virtual environment using
        
            $ python3 -m venv venv_name 
    - Activate Virtual Environment (example : windows)

            $ .\venv\Scripts\Activate.ps1

- Install requirements.txt file

        $ pip install -r ./requirements.txt

- to run the web app

        $ python ./app.py

the application will display the url on which the app is running and where it can be accessed at within the terminal output.