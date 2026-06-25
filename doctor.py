class Doctor:

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"