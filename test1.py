class etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_informations(self):
        print(f"Nom: {self.nom}")
        print(f"Age: {self.age}")
        print(f"Note: {self.note}")

    def modifier_note(self, nouvelle_note):
        self.note = nouvelle_note

# Create an etudiant object
etudiant1 = etudiant("Alice", 20, 85)

etudiant1.afficher_informations()

# Modify the student's grade
etudiant1.modifier_note(90)

etudiant1.afficher_informations()
