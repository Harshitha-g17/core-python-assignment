def search_by_disease(patients, disease):
    matching_patients = [patient["Name"] for patient in patients if patient["Disease"] == disease]
    return matching_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
print(f"Patients with {search_disease}:{search_by_disease(patients,search_disease)}")
