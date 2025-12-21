class student:
    def __init__(self, name, average_score):
        self.name = name
        self.average_score = average_score
    
    def is_excellent(self):
        if self.average_score == 5:
            return True
        else:
            return False

student1 = student("заур", 4.5)
student2 = student("степан", 5)

print(student1.is_excellent())
print(student2.is_excellent())