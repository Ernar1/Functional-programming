#1
'''
#list
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
University.clear()
print(University)
#cor
user = ("Mazhenov Ernar", 20, "Student")
for item in user:
    print(item) 
input()

#set
stud = set(["Mazhenov Ernar", "Student", "20"]) 
stud.add("Programmist") 
print(stud)
'''

#2
'''
cor = (1,2,3,4,5,6,7,8,9,10)
print(cor[1:5])



A = ("ab", "ac", "ab", "ab", "ca", "ad", "jklmn")
d1 = A.count("ab") 
d2 = A.count("jprst")
d3 = A.count("ca")  
print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)

A = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
day = str(input("Enter day: "))
if day in A: 
    num = A.index(day)
    print("Number of day = ", num + 1)
else:
    num = -1
    print("Wrong day.")


my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([4, 5], {1, 6, 8})
print(my_set)

my_set1 = set("HelloWorld")
print(my_set1)

print(my_set1.pop())

my_set1.clear()
print(my_set1)
'''

#3
dict = {"Hello": "Hi", "Goodbye": "Bye"}

temp = []
for i in dict: temp.append(i)

INPUT = input("Введите слово\n>>> ").lower()
for i in range(len(temp)):
    if i == len(temp): print("Синонима нет"); 
    
    if temp[i] .lower() == INPUT:
     for n in dict:
      if n == temp[i]:
       print(dict[n])