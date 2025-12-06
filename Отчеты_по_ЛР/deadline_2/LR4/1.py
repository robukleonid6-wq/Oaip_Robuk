grades = []

grades.append(5)
grades.append(2)
grades.append(2)
grades.append(3)
grades.append(4)

print(f'Текущие оценки: {grades}')

dsdfs = sum(grades) / len(grades)

del grades[0]
del grades[3]

print(f'Средний балл: {dsdfs}')
print(f'Итоговые оценки: {grades}')