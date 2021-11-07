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