class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def get_name(self):
        return self._name

    def set_name(self, newname):
        self._name = newname


    def get_surname(self):
        return self.surname

    def set_surname(self, newsurname):
        self._surname = newsurname

david = Person("david", "Jimenez Sequero")
david._name = "Bob"

henry = Person("henry", "Bushell")
print(henry.get_name())
print(david.get_name())
