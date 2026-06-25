from patient import Patient
from doctor import Doctor
from appointment import Appointment
from specialization import Specialization


class OperationsManager:

    def __init__(self):

        self.specializations = {
            1: Specialization("Cardiology"),
            2: Specialization("Neurology"),
            3: Specialization("Orthopedics")
        }

        self.doctors = [
            Doctor("Sharma", "Cardiology"),
            Doctor("Verma", "Neurology"),
            Doctor("Singh", "Orthopedics")
        ]

        self.appointments = []

    def add_patient(self):

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")

        print("0 = Normal")
        print("1 = Urgent")
        print("2 = Super Urgent")

        status = int(input("Enter Status: "))

        patient = Patient(
            name,
            age,
            disease,
            status
        )

        print("\nSpecializations")
        print("1. Cardiology")
        print("2. Neurology")
        print("3. Orthopedics")

        spec = int(input("Choose: "))

        self.specializations[spec].add_patient(patient)

        with open("patients.txt", "a") as file:
            file.write(str(patient) + "\n")

        print("Patient Added Successfully")

    def show_patients(self):

        for specialization in self.specializations.values():

            print(f"\n**  {specialization.name} **")

            specialization.list_patients()

    def search_patient(self):

        name = input("Enter Patient Name: ")

        for specialization in self.specializations.values():

            patient = specialization.search_patient(name)

            if patient:
                print(patient)
                return

        print("Patient Not Found")

    def remove_patient(self):

        name = input("Enter Patient Name: ")

        for specialization in self.specializations.values():

            if specialization.remove_patient(name):
                print("Patient Removed")
                return

        print("Patient Not Found")

    def next_patient(self):

        print("\n1. Cardiology")
        print("2. Neurology")
        print("3. Orthopedics")

        spec = int(input("Choose Specialization: "))

        patient = self.specializations[spec].get_next_patient()

        if patient:
            print("\nNext Patient:")
            print(patient)
        else:
            print("No Patient in Queue")

    def book_appointment(self):

        patient_name = input(
            "Enter Patient Name: "
        )

        found_patient = None

        for specialization in self.specializations.values():

            patient = specialization.search_patient(
                patient_name
            )

            if patient:
                found_patient = patient
                break

        if not found_patient:
            print("Patient Not Found")
            return

        print("\nDoctors")

        for index, doctor in enumerate(
                self.doctors,
                start=1):
            print(index, doctor)

        choice = int(
            input("Choose Doctor: ")
        )

        doctor = self.doctors[choice - 1]

        appointment = Appointment(
            found_patient,
            doctor
        )

        self.appointments.append(
            appointment
        )

        print("Appointment Booked")

    def show_appointments(self):

        if not self.appointments:
            print("No Appointments")
            return

        for appointment in self.appointments:
            print(appointment)

    def hospital_report(self):

        total = 0
        normal = 0
        urgent = 0
        super_urgent = 0

        for specialization in self.specializations.values():

            for patient in specialization.patients:

                total += 1

                if patient.status == 0:
                    normal += 1
                elif patient.status == 1:
                    urgent += 1
                else:
                    super_urgent += 1

        print("\nHospital Report")
        print("Total Patients:", total)
        print("Normal:", normal)
        print("Urgent:", urgent)
        print("Super Urgent:", super_urgent)