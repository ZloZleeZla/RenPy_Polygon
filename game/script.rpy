# Вы можете расположить сценарий своей игры в этом файле.

init python:
    import random
    from characterClass import MainCharacter
    def check(param, discipline, modif=0, skill=0):  # Функция проверки, skill=навык, param=характеристика, mod=модификатор
        global quantityDices, result, successes # Нужно объявить, что ты работаешь с глобальными переменными, иначе нихера не измениться
        quantityDices = skill + param + modif + discipline # Количество бросков
        dices = [random.randint(1, 6) for i in range(quantityDices)] # Генерация бросков
        result = " ".join([str(res) for res in dices]) # Формирование строки результата. [2, 5, 4] -> 2 5 4
        successes = dices.count(5) + dices.count(6) # Подсчет успехов

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
# define это ебучая константа, нужно объявлять изменяемые переменные через default
# ну или сразу задавать им значение через define
default result = ""
default successes = ""
default quantityDices = ""

# Создание Брухи
default clan = ""
default params = ""
default skills = ""
default disciplines = ""

$ clan = "Бруха"
$ params = {'strength': 4, 'intellect': 1}
$ skills = {'brawler': 3, 'fighting': 5, 'knowledge': 1}
$ disciplines = {'power': 3, 'resistance': 2}

default mc_bruha = MainCharacter(clan="Бруха", params=params, skills=skills, disciplines=disciplines)
# Игра начинается здесь:
label start:

    scene bg room

    # Вставка значения х в строку
    # e "Красава дай [x]" 
    
    e "О, ты из клана [mc_bruha.clan]"
    e "У тебя сила [mc_bruha.params['strength']], знание [mc_bruha.skills['knowledge']], дисциплина [mc_bruha.disc['power']]"
    $ check(mc_bruha.params['strength'], 0, mc_bruha.skills['knowledge'], mc_bruha.disc['power'])
    e "Итого [quantityDices] d6. Бросок [result] -> Успехов [successes]"

    jump start

    return
