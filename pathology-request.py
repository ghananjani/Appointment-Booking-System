@app.route('/request_pathology', methods=['GET', 'POST'])
def request_pathology():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        test_id = request.form['test_id']
        test_date = request.form['test_date']

        cursor.execute(
            "INSERT INTO PatientTests (patient_id, test_id, test_date) VALUES (%s, %s, %s)",
            (patient_id, test_id, test_date)
        )
        db.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    cursor.execute("SELECT * FROM LabTests WHERE test_type = 'Pathology'")
    tests = cursor.fetchall()
    return render_template('request_pathology.html', patients=patients, tests=tests)
