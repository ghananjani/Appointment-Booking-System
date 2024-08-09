CREATE TABLE PatientTests (
    patient_test_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    test_id INT,
    test_date DATETIME,
    result TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (test_id) REFERENCES LabTests(test_id)
);
