from random import randint

class buyer:
    def __init__(self, surname, name, secsurname, adress, numbercred, numberbank):
        self.__surname=surname
        self.__name = name
        self.__secsurname = secsurname
        self.__adress = adress
        self.__numbercred = numbercred
        self.__numberbank = numberbank

    def update(self, p):
        s = input('Напишите, что хотите поменять в данных')
        if s == 'Фамилия' or 'фамилия':
            self.__surname=input("Введите фамилию")
        elif s == 'Имя' or 'имя':
            self.__name=input("Введите имя")
        elif s == 'Отчество' or 'отчество':
            self.__secsurname=input("Введите отчество")
        elif s == 'Адрес' or 'адрес':
            self.__adress=input("Введите адрес")
        elif s == 'Номер банковской карты' or 'номер банковской карты':
            self.__numbercred=input("Введите номер банковской карты")
        elif s == 'Банковский счет' or 'банковский счет':
            self.__numberbank=input("Введите банковский счет")
    def get(self):
        s=input("Что вы хотите вернуть")
        if s == 'Фамилия' or 'фамилия':
            return self.__surname
        elif s == 'Имя' or 'имя':
            return self.__name
        elif s == 'Отчество' or 'отчество':
            return self.__secsurname
        elif s == 'Адрес' or 'адрес':
            return self.__adress
        elif s == 'Номер банковской карты' or 'номер банковской карты':
            return self.__numbercred
        elif s == 'Банковский счет' or 'банковский счет':
            return self.__numberbank
    def info(self):
        print("Имя: "+self.__name+" Фамилия: "+self.__surname+" Отчество: "+self.__secsurname+" Адрес: "+self.__adress+" Номер банковской карты: "+self.__numbercred+" Банковский счет: "+self.__numberbank)

someCustomer = buyer(name='', surname='', secsurname='', adress='', numbercred='', numberbank='')
someCustomer.update(someCustomer)
someCustomer.update(someCustomer)
someCustomer.update(someCustomer)
someCustomer.update(someCustomer)
someCustomer.update(someCustomer)
someCustomer.update(someCustomer)
someCustomer.get(someCustomer)
someCustomer.info(someCustomer)