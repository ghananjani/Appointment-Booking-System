from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="medical_centre"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# New Patient Registration Form
@app.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact_number = request.form['contact_number']
        email = request.form['email']
        address = request.form['address']

        cursor.execute(
            "INSERT INTO Patients (first_name, last_name, dob, gender, contact_number, email, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, dob, gender, contact_number, email, address)
        )
        db.commit()
        return redirect(url_for('index'))
    return render_template('register_patient.html')

# More routes and functions to be added for Appointments, Lab Tests, etc.

if __name__ == '__main__':
    app.run(debug=True)
