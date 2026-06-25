class Appointment:

    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

    def __str__(self):
        return (f"Patient: {self.patient.name} "
                f"--> Doctor: {self.doctor.name}")