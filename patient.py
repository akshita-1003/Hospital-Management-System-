class Patient:
    patient_count = 1

    def __init__(self, name, age, disease, status):
        self.id = Patient.patient_count
        Patient.patient_count += 1

        self.name = name
        self.age = age
        self.disease = disease
        self.status = status

    def get_status(self):
        if self.status == 0:
            return "Normal"
        elif self.status == 1:
            return "Urgent"
        else:
            return "Super Urgent"

    def __str__(self):
        return (f"ID: {self.id} | "
                f"Name: {self.name} | "
                f"Age: {self.age} | "
                f"Disease: {self.disease} | "
                f"Status: {self.get_status()}")