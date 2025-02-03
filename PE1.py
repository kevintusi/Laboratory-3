# student.py

class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"Student('{self.name}')"

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Cannot compare Student to non-Student")
        return self.name < other.name

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Cannot compare Student to non-Student")
        return self.name >= other.name

def main():
    student1 = Student("Kevin")
    student2 = Student("Angelo")
    student3 = Student("Kevin")

    print("Equality test:")
    print(student1 == student2)  # Should print False
    print(student1 == student3)  # Should print True

    print("\nLess than test:")
    print(student1 < student2)  # Should print True
    print(student2 < student1)  # Should print False

    print("\nGreater than or equal to test:")
    print(student1 >= student2)  # Should print False
    print(student2 >= student1)  # Should print True
    print(student1 >= student3)  # Should print True

if __name__ == "__main__":
    main()
