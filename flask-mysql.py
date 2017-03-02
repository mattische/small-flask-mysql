from flask import Flask, render_template
import mysql.connector
from flask import request


app = Flask(__name__)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route('/')
def hello_world():
    con = mysql.connector.connect(user='dbuser', password='password123', host='194.47.143.131',
                                  database='classicmodels')
    cursor = con.cursor()
    cursor.execute("SELECT employeeNumber, firstName, lastName FROM employees")
    res = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template("template.html", employees=res)


@app.route('/employee/<empNbr>')
def employee(empNbr):
    con = mysql.connector.connect(user='dbuser', password='password123', host='194.47.143.131',
                                  database='classicmodels')
    cursor = con.cursor()

    cursor.execute("SELECT employeeNumber, firstName, lastName FROM employees WHERE employeeNumber="+empNbr)
    res = cursor.fetchone()
    cursor.close()
    con.close()
    return render_template("employee.html", employee=res)


@app.route('/update_employee', methods=['POST'])
def addRegion():
    print("update employee...")
    e = (request.form['e_nbr'], request.form['e_fname'], request.form['e_lname'], True)
    return render_template("employee.html", employee=e)

if __name__ == '__main__':
    app.run()
