# Вы можете расположить сценарий своей игры в этом файле.

# init python:
#     import random
#     from characterClass import MainCharacter
#     def check(param, discipline, modif=0, skill=0):  # Функция проверки, skill=навык, param=характеристика, mod=модификатор
#         global quantityDices, result, successes # Нужно объявить, что ты работаешь с глобальными переменными, иначе нихера не измениться
#         quantityDices = skill + param + modif + discipline # Количество бросков
#         dices = [random.randint(1, 6) for i in range(quantityDices)] # Генерация бросков
#         result = " ".join([str(res) for res in dices]) # Формирование строки результата. [2, 5, 4] -> 2 5 4
#         successes = dices.count(5) + dices.count(6) # Подсчет успехов

# # Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")
# # define это ебучая константа, нужно объявлять изменяемые переменные через default
# # ну или сразу задавать им значение через define
# default result = ""
# default successes = ""
# default quantityDices = ""

# # Создание Брухи
# default clan = ""
# default params = ""
# default skills = ""
# default disciplines = ""

# $ clan = "Бруха"
# $ params = {'strength': 4, 'intellect': 1}
# $ skills = {'brawler': 3, 'fighting': 5, 'knowledge': 1}
# $ disciplines = {'power': 3, 'resistance': 2}

# default mc_bruha = MainCharacter(clan="Бруха", params=params, skills=skills, disciplines=disciplines)
# Игра начинается здесь:

init python:
    # Базовые характеристики персонажа
    default_character = {
        "name": "",
        "gender": "male",
        "hair_color": "brown",
        "eye_color": "blue",
        "outfit": "casual",
        "personality": "friendly"
    }
    
    # Создаем словарь для хранения выборов игрока
    player_character = default_character.copy()


screen character_creation():
    modal True
    
    frame:
        xfill True
        yfill True
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            text "Character Creation" size 40 xalign 0.5
            
            # Имя персонажа
            vbox:
                text "Name:"
                input default "" value ScreenVariableInputValue("player_character['name']")
            
            # Выбор пола
            vbox:
                text "Gender:"
                hbox:
                    textbutton "Male" action SetDict(player_character, "gender", "male")
                    textbutton "Female" action SetDict(player_character, "gender", "female")
            
            # Выбор цвета волос
            vbox:
                text "Hair Color:"
                hbox:
                    for color in ["brown", "black", "blonde", "red"]:
                        textbutton color action SetDict(player_character, "hair_color", color)
            
            # Выбор цвета глаз
            vbox:
                text "Eye Color:"
                hbox:
                    for color in ["blue", "green", "brown", "gray"]:
                        textbutton color action SetDict(player_character, "eye_color", color)
            
            # Выбор одежды
            vbox:
                text "Outfit:"
                hbox:
                    for outfit in ["casual", "formal", "sporty"]:
                        textbutton outfit action SetDict(player_character, "outfit", outfit)
            
            # Предпросмотр персонажа
            frame:
                xsize 300
                ysize 400
                xalign 0.5
                
                add "character_preview" # Здесь должно быть изображение персонажа
            
            # Кнопки управления
            hbox:
                spacing 20
                xalign 0.5
                textbutton "Reset" action SetVariable("player_character", default_character.copy())
                textbutton "Confirm" action Return()


label start:

    scene bg room

#     # Вставка значения х в строку
#     # e "Красава дай [x]" 
    
#     e "О, ты из клана [mc_bruha.clan]"
#     e "У тебя сила [mc_bruha.params['strength']], знание [mc_bruha.skills['knowledge']], дисциплина [mc_bruha.disc['power']]"
#     $ check(mc_bruha.params['strength'], 0, mc_bruha.skills['knowledge'], mc_bruha.disc['power'])
#     e "Итого [quantityDices] d6. Бросок [result] -> Успехов [successes]"

#     jump start

#     return



    # scene bg room
    
    show lsf
    # e "Где-то здесь должен быть чарник"

    return

