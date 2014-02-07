#coding=utf-8
'''
ИТАК, САМА ЗАДАЧА
Построить три класса (базовый и 2 потомка), описывающих некоторых работников с почасовой оплатой
(один из потомков) и фиксированной оплатой (второй потомок). Описать в базовом классе абстрактный метод
для расчета среднемесячной заработной платы. Для «повременщиков» формула для расчета такова:
«среднемесячная заработная плата = 20.8 * 8 * почасовую ставку», для работников с фиксированной оплатой
«среднемесячная заработная плата = фиксированной месячной оплате».
a) Упорядочить всю последовательность работников по убыванию среднемесячного заработка. При совпадении
зарплаты – упорядочивать данные по алфавиту по имени. Вывести идентификатор работника, имя и среднемесячный
заработок для всех элементов списка.
b) Вывести первые 5 имен работников из полученного в пункте а) списка.
c) Вывести последние 3 идентификатора работников из полученного в пункте а) списка.
d) Организовать запись и чтение коллекции в/из файл.
e) Организовать обработку некорректного формата входного файла.
'''

class Worker():                                               # Superclass of all worker

    def __init__(self, name, post):
        self.name = name
        self.post = post

    def average_salary(self):                                 # function calculate the average monthly salary
        pass                                                  # abstract


class Worker_time(Worker):                                    # Subclass of employees with hourly salary
    def __init__(self, name, post, sal):
        Worker.__init__(self, name, post)
        self.sal = sal
        self.average_sal = Worker_time.salary (self)
        global all_people
        all_people.append([self.name, self.post, self.average_sal])

    def salary(self):
        return self.sal*20*8

class Worker_fix(Worker):                                                # Subclass of employees with fixed salaries
    def __init__(self, name, post, sal_fix ):
        Worker.__init__(self, name, post)
        self.sal_fix = sal_fix
        self.average_sal = Worker_fix.salary(self)
        global all_people
        all_people.append([self.name, self.post, self.average_sal])

    def salary(self):
        return self.sal_fix


def sorter(items):                                                      # function sorting of worker by their salary
        items = sorted(items, key=lambda x: x[2],reverse=True)
        print items
        return items


def print_all (items):                                                  # Displaing all worker
    for i in items:
        print i[0], '--- $', i[2]
    print '*'*20

def print_X (items, rev=False, N=5):                                 # Displaying N workers with or without reverse
    step=0
    if rev == True:
        items = reversed(items)
    for i in items:
        print i[0], '--- $', i[2]
        step+=1
        if step>N-1: break
    print '*'*20
all_people = []


if __name__=='__main__':                                                 # Tests for control

    Ivan = Worker_time('Ivan', 'programmer',10)
    Ivan1 = Worker_time('Ivan1', 'programmer',13)
    Ivan2 = Worker_time('Ivan2', 'programmer',6)
    Ivan3 = Worker_time('Ivan3', 'programmer',20)
    Ivan4 = Worker_time('Ivan4', 'programmer',8)
    Ivan5 = Worker_time('Ivan5', 'programmer',11)
    Petr = Worker_fix('Petr','programmer',1000)
    Petr1 = Worker_fix('Petr1','programmer',1000)
    Petr2 = Worker_fix('Petr2','programmer',2000)
    Petr3 = Worker_fix('Petr3','programmer',900)
    Petr4 = Worker_fix('Petr4','programmer',1110)
    Petr5 = Worker_fix('Petr5','programmer',1100)
    Sem2 = Worker_fix('Sem2','programmer',1000)
    Sem1 = Worker_fix('Sem1','programmer',1000)


    all_woker_sort = sorter(all_people)

    print_all(all_woker_sort)

    print_X(all_woker_sort, N=5)

    print_X(all_woker_sort,rev=True, N=3)




