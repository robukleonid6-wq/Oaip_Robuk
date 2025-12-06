studenty = [
    ("Прохор", 21, 5.0),
    ("заур", 22, 2.2),
    ("саня(водолаз)", 19, 4.8),
    ("Бурцев", 20, 3.3),
    ("Павел", 23, 4.9)
]

print("студенты старше 20 лет:")
for student in studenty:
    imya, vozrast, ball = student
    if vozrast > 20:
        print(f"- {imya} ({vozrast}), средний балл: {ball}")

luchshiy_student = studenty[0]
for student in studenty:
    if student[2] > luchshiy_student[2]:
        luchshiy_student = student

print(f"лучший студент: {luchshiy_student[0]}, средний балл: {luchshiy_student[2]}")

otsortirovannye_studenty = []
for student in studenty:
    otsortirovannye_studenty.append(student)

for i in range(len(otsortirovannye_studenty)):
    for j in range(len(otsortirovannye_studenty) - 1 - i):
        if otsortirovannye_studenty[j][0] > otsortirovannye_studenty[j + 1][0]:
            temp = otsortirovannye_studenty[j]
            otsortirovannye_studenty[j] = otsortirovannye_studenty[j + 1]
            otsortirovannye_studenty[j + 1] = temp

print("студенты отсортированные по имени:")
for student in otsortirovannye_studenty:
    print(f" {student[0]}, возраст: {student[1]}, балл: {student[2]}")
print()