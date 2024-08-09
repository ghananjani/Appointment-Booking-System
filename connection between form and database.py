if request.method == 'POST':
    first_name = request.form['first_name']
    # Other form fields...
    cursor.execute(
        "INSERT INTO Patients (first_name, ...) VALUES (%s, ...)",
        (first_name, ...)
    )
    db.commit()
