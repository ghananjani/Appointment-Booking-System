@app.route('/input_lab_results', methods=['GET', 'POST'])
def input_lab_results():
    if request.method == 'POST':
        patient_test_id = request.form['patient_test_id']
        result = request.form['result']

        cursor.execute(
            "UPDATE PatientTests SET result = %s WHERE patient_test_id = %s",
            (result, patient_test_id)
        )
        db.commit()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM PatientTests WHERE result IS NULL")
    patient_tests = cursor.fetchall()

    return render_template('input_lab_results.html', patient_tests=patient_tests)
