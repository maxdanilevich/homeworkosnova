print("Задача 72")
coun = ['Математика', 'Русский', 'Белорусский', 'Информатика', 'Биология', 'Английский']
for country in coun:
    print(country)
iyuy=input("Введите какие предметы вам не нравятся: ")
if iyuy=='Математика':
    coun.pop(0)
if iyuy=='Русский':
    coun.pop(1)
if iyuy=='Белорусский':
    coun.pop(2)
if iyuy=='Информатика':
    coun.pop(3)
if iyuy=='Биология':
    coun.pop(4)
if iyuy=='Английский':
    coun.pop(5)
for country in coun:
    print(country)
print("Задача 74")
color=['Фиолетовый','Красный','Желтый','Синий','Серый','Черный','Белый','Пурпурный','Голубой','Зеленый']
x=int(input("Выберите число от 0 до 4"))
y=int(input("Выберите число от 5 до 9"))
del color[0:x]
del color[y-1:9]
print(color)
print("Задача 75")
chisla=[123,456,789,458]
print(chisla)
a=int(input("Введите трехзначное число"))
if a==chisla[0]:
    print(1)
elif a==chisla[1]:
    print(2)
elif a==chisla[2]:
    print(3)
elif a==chisla[3]:
    print(4)
else:
    print("That is not in the list")
print("Задача 76")
w=input("введите имя первого человека: ")
y=input("введите имя второго человека: ")
t=input("введите имя третьего человека: ")
rty=[w,y,t]
while True:
    word=input("Хотите позвать еще одного человека?")
    if word=="yes":
        o=input("Введите имя человека, которого хотите позвать: ")
        rty.append(o)
    if word=="no":
        break;
print(len(rty))