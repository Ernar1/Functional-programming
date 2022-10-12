#1
""""
def is_sorted(lst):
    if lst == sorted(lst):
        return True
    elif lst == sorted(lst, reverse=True):
        return False
print(is_sorted(['a', 'b', 'c', 'd']))
"""

#2
''''
name = ['Mazhenov Ernar']
course = [4]
gpa = [2.9]
age = [20]
print("Резюме: \n", name)
print(course)
print(gpa)
print(age)
'''

#3
''''
students = [
        ('Mazhenov Ernar', 3),
        ('Auezov Abzal', 4),
        ('Kanagatov Murat', 2),
        ('Aitkali Azamat', 1)
    ]
print(sorted(students, key=lambda v: (v[1])))
[('fio3', 1), ('fio0', 1), ('fio2', 1), ('fio1', 2)]
'''