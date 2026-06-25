class Specialization:

    MAX_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):

        if len(self.patients) >= self.MAX_CAPACITY:
            print("Queue is Full!")
            return

        self.patients.append(patient)

        self.patients.sort(
            key=lambda p: p.status,
            reverse=True
        )

    def get_next_patient(self):

        if not self.patients:
            return None

        return self.patients.pop(0)

    def remove_patient(self, patient_name):

        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                self.patients.remove(patient)
                return True

        return False

    def search_patient(self, patient_name):

        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                return patient

        return None

    def list_patients(self):

        if not self.patients:
            print("No Patients")

        for patient in self.patients:
            print(patient)