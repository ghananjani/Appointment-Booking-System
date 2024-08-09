@app.route('/prescribe_medication', methods=['GET', 'POST'])
def prescribe_medication():
    if request.method == 'POST':
        appointment_id = request.form['appointment_id']
        medication = request.form['medication']
        dosage = request.form['dosage']
        frequency = request.form['frequency']

        cursor.execute(
            "INSERT INTO Prescriptions (appointment_id, medication, dosage, frequency) VALUES (%s, %s, %s, %s)",
            (appointment_id, medication, dosage, frequency)
        )
        db.commit()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM Appointments WHERE status = 'Completed'")
    appointments = cursor.fetchall()

    return render_template('prescribe_medication.html', appointments=appointments)
