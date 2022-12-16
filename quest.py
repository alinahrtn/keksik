import random
money  = 50
health = 50
eda = 50
quest = 50

while money>0 or health>30 or eda>0 or quest>40:
    time = 1
    print("Деньги ", money)
    print("Здоровье ", health)
    print("Сытость ", eda)
    print("Успеваемость", quest)
    if time==1:
        print("Наступил день")
        print("Что хочешь сделать?")
        print("1. Идти на пары")
        print("2. Работать")
        print("3. Закрывать долги")
        v1 = int(input())
        #if v1!=1 or v1!=2 or v1!=3:
        #    print("Ты ввел что-то не то, введи нормально пж")
        #    v1 = int(input())
        if v1==1:
            print("Как ты хочешь добраться до уника?")
            print("1. Пешком")
            print("2. Поехать")
            v2 = int(input())
        #    if v2 != 1 or v2 != 2:
        #        print("Ты ввел что-то не то, введи нормально пж")
        #       v2 = int(input())
            if v2==1:
                print("Ты дошел до уника")
                healt=health-30
                eda = eda-15
                time=time-1
                print("Деньги ", money)
                print("Здоровье ", health)
                print("Сытость ", eda)
                print("Успеваемость", quest)
            elif v2==2:
                print("Ты доехал до уника")
                money=money-5
                luck1 = random.randint(0, 100)
                if luck1<15:
                    health=health-30
                    print("Ты заболел в автобусе!!!!!!")
                time=time-1
                print("Деньги ", money)
                print("Здоровье ", health)
                print("Сытость ", eda)
                print("Успеваемость", quest)
        elif v1==2:
            print("Ты поработал")
            money = money+30
            quest = quest-5
            eda = eda-15
            health = health -5
            time = time - 1
            print("Деньги ", money)
            print("Здоровье ", health)
            print("Сытость ", eda)
            print("Успеваемость", quest)
        elif v1==3:
            print("Какие ты хочешь закрыть долги")
            print("1. Легкие")
            print("2. Средненькие")
            print("3. Страшные")
            v3 = int(input())
        #    if v3 != 1 or v3 != 2 or v3!=3:
        #        print("Ты ввел что-то не то, введи нормально пж")
        #        v3 = int(input())
            if v3 ==1:
                luck2= random.randint(0, 100)
                if luck2<60:
                    print("Ты закрыл легкий долг")
                    quest = quest+10
                    eda = eda -10
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
                else:
                    print("Ты не закрыл легкий долг")
                    eda = eda-10
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
            if v3 ==2:
                luck3= random.randint(0, 100)
                if luck3<40:
                    print("Ты закрыл нормальный долг")
                    quest = quest+20
                    eda = eda -10
                    health = health -5
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
                else:
                    print("Ты не закрыл нормальный долг")
                    eda = eda-10
                    health = health - 5
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
            if v3 ==3:
                luck4= random.randint(0, 100)
                if luck4<20:
                    print("Ты закрыл ужасный долг")
                    quest = quest+40
                    eda = eda -10
                    health = health -10
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
                else:
                    print("Ты не закрыл ужасный долг")
                    eda = eda-10
                    health = health - 10
                    time = time - 1
                    print("Деньги ", money)
                    print("Здоровье ", health)
                    print("Сытость ", eda)
                    print("Успеваемость", quest)
    if time ==0:
        print("Наступила ночь")
        time=time+1
    if quest==100:
        print("Ты выиграл!!!!!!")
        exit()

print("Лох, отчислен")
