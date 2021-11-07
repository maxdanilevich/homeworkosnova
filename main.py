print("Задача 77")
w=input("введите имя первого человека: ")
y=input("введите имя второго человека: ")
t=input("введите имя третьего человека: ")
rty=[w,y,t]
print(rty)
while True:
    word=input("Хотите позвать еще одного человека?")
    if word=="yes":
        o=input("Введите имя человека, которого хотите позвать: ")
        rty.append(o)
    if word=="no":
        break;
print(rty)
while True:
    word1=input("Введите имя человека из списка")
    k=(rty.index(word1))
    print(k+1)
    message=input("Хотите ли вы, чтобы этот человек присутствовал на вечеринке")
    if message=="no":
        rty.pop(k)
        break;
print(rty)

print("Задача 78")
tv=["Major","Gdechtokogda","Pogoda","News"]
for i in tv:
    print(i)
fy=input("Введите название еще одной программы")
gy=int(input("введите позицию этой программы в списке"))
tv.insert(gy-1,fy)
for i in tv:
    print(i)

print("Задача 79")
nums=[]
o=0
while True:
    o+=1
    u=int(input("Введите число"))
    nums.append(u)
    if o==3:
        question=input("Хотите ли вы оставить последнее введенное число в списке?")
        if question=="no":
            nums.pop(2)
            break;
print(nums)
