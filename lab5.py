#1
'''
name = ['Mazhenov Ernar']
age = [20]
name.append('ernarmazhenov2000@gmail.com')
print("Резюме: \n", name)
print(age)
University = [ 'Name: Satbayev University',
'Course: 4',
'Gpa: 2.9',
'Entry year: 2019',
'Ending year: 2023' ]
University.insert(1,'Department: Programm engineering')
print(University)
'''
#2
'''
students = [
        ('Mazhenov Ernar', 3),
        ('Auezov Abzal', 4),
        ('Kanagatov Murat', 2),
        ('Aitkali Azamat', 1)
    ]
print(sorted(students, key=lambda v: (v[1])))
[('Mazhenov Ernar', 3), ('Auezov Abzal', 4), ('Kanagatov Murat', 2), ('Aitkali Azamat', 1)]
'''

#3
'''
student = ['Mazhenov Ernar']
student1 = ['Auezov Abzal']
student2 = ['Rayimbek Muzameluly']
grade = [4]
grade1 = [5]
grade2 = [4]
print('Student name: ',student,f'Student grade: {grade}')
print('Student name: ',student1,f'Student grade: {grade1}')
'''
#4
''''
my_list = []
while True:
  n = int(input('Введите число: '))
  if(n!=0):
    my_list.append(n)
  else:
    listSort = sorted(list)
    for i in listSort:
      print(i)
    break
'''


