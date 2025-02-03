import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"

    def __lt__(self, other):
        """Returns self < other, with respect to names."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns self >= other, with respect to names."""
        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():
    """Tests sorting."""
    # Create the list and put 8 students into it
    names = {'Vera', 'Andrei', 'Karyl', 'Kevin', 'Alexa', 'Jehu', 'jake', 'Michael', 'William', 'Elly', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel'}
    lyst = []

    for _ in range(8):
        name = random.choice(list(names))
        names.remove(name)
        s = Student(name, 3)
        lyst.append(s)

    # Print unsorted list
    print('Unsorted list:')
    for s in lyst:
        print(s)
    
    # Sort the list
    lyst.sort()
    
    # Print sorted list
    print('\nSorted list:')
    for s in lyst:
        print(s)

if __name__ == "__main__":
    main()
