from flask import Flask, render_template, request, redirect, url_for
import models

app = models.app
db = models.db

t_employee = models.Employee
t_departments = models.Departments

flag = True

with app.app_context():
    db.create_all()
    
def populate():
  
    emp_1 = t_employee(first_name='Praveen', last_name='S', email_address='iamprvn.s@gmail.com', phone='9988774455', salary='99,00,000')
    db.session.add(emp_1)

    emp_2 = t_employee(first_name='Sheldon', last_name='Cooper', email_address='sheldonor@gmail.com', phone='9988774455', salary='73,73,737')
    db.session.add(emp_2)

    emp_3 = t_employee(first_name='Leonard', last_name='Hofstadter', email_address='iamnotleakey@gmail.com', phone='9988774455', salary='72,00,000')
    db.session.add(emp_3)

    emp_4 = t_employee(first_name='	Howard', last_name='Wolowitz', email_address='austronautWolowitz@gmail.com', phone='9988774455', salary='69,42,000')
    db.session.add(emp_4)

    emp_5 = t_employee(first_name='Rajesh', last_name='Koothrappali', email_address='brown.dynamite@gmail.com', phone='9988774455', salary='1,00,00,000')
    db.session.add(emp_5)

    dep_1 = t_departments(dept_name='Production')
    db.session.add(dep_1)

    dep_2 = t_departments(dept_name='Developer')
    db.session.add(dep_2)

    dep_3 = t_departments(dept_name='Marketing')
    db.session.add(dep_3)

    dep_4 = t_departments(dept_name='R & D')
    db.session.add(dep_4)

    db.session.commit()

@app.route("/",methods=['GET','POST'])
def home():
    populate()
    return render_template('index.html')


@app.route("/assignment",methods=['GET','POST'])
def assignment():

    if request.method == 'POST':
        department_id = request.form['dept_select']
        emp_id = request.form['emp_id']
        employee = t_employee.query.filter_by(id=emp_id).first()
        employee.dept_id = department_id

        db.session.commit()

        print(employee)
        
    emp_vals = t_employee.query.all()
    dept_vals = t_departments.query.all()
    
    return render_template("table.html", employees=emp_vals, departments=t_departments, department_names=dept_vals)



# @app.route("/test")
# def test():
#     results = t_employee.query.all()
#     return str(results[0].first_name)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)