from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'culturemonkeyassignment'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db = SQLAlchemy(app)

class Departments(db.Model):

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String, nullable=True)

    def __init__(self, dept_name) -> None:
        super().__init__()
        self.dept_name = dept_name


    def __repr__(self) -> str:
        return f"Departments('{self.id}','{self.dept_name}')"
    
class Employee(db.Model):

    __tablename__ = "employee"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    email_address = db.Column(db.String,  nullable=False)
    phone = db.Column(db.String)
    salary = db.Column(db.String)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False, default=1)

    def __init__(self, first_name, last_name, email_address, phone, salary, dept_id = 1) -> None:
        super().__init__()
        self.first_name = first_name 
        self.last_name = last_name
        self.email_address = email_address
        self.phone = phone
        self.salary = salary
        self.dept_id = dept_id

        

    def __repr__(self) -> str:

        res = {}
        res[self.id] = {}
        res[self.id]['first_name'] = self.first_name 
        res[self.id]['last_name'] = self.last_name
        res[self.id]['email_address'] = self.email_address
        res[self.id]['phone'] = self.phone
        res[self.id]['salary'] = self.salary
        res[self.id]['dept_id'] = self.dept_id

        return str(res)

