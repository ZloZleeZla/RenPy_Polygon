# {
#     # Вы можете расположить сценарий своей игры в этом файле.

#     # init python:
#     #     import random
#     #     from characterClass import MainCharacter
#     #     def check(param, discipline, modif=0, skill=0):  # Функция проверки, skill=навык, param=характеристика, mod=модификатор
#     #         global quantityDices, result, successes # Нужно объявить, что ты работаешь с глобальными переменными, иначе нихера не измениться
#     #         quantityDices = skill + param + modif + discipline # Количество бросков
#     #         dices = [random.randint(1, 6) for i in range(quantityDices)] # Генерация бросков
#     #         result = " ".join([str(res) for res in dices]) # Формирование строки результата. [2, 5, 4] -> 2 5 4
#     #         successes = dices.count(5) + dices.count(6) # Подсчет успехов

#     # # Определение персонажей игры.
#     # define e = Character('Эйлин', color="#c8ffc8")
#     # # define это ебучая константа, нужно объявлять изменяемые переменные через default
#     # # ну или сразу задавать им значение через define
#     # default result = ""
#     # default successes = ""
#     # default quantityDices = ""

#     # # Создание Брухи
#     # default clan = ""
#     # default params = ""
#     # default skills = ""
#     # default disciplines = ""

#     # $ clan = "Бруха"
#     # $ params = {'strength': 4, 'intellect': 1}
#     # $ skills = {'brawler': 3, 'fighting': 5, 'knowledge': 1}
#     # $ disciplines = {'power': 3, 'resistance': 2}

#     # default mc_bruha = MainCharacter(clan="Бруха", params=params, skills=skills, disciplines=disciplines)
#     # Игра начинается здесь:

#     init python:
#     # Базовые характеристики персонажа
#     default_character = {
#         "name": "",
#         "gender": "male",
#         "hair_color": "brown",
#         "eye_color": "blue",
#         "outfit": "casual",
#         "personality": "friendly"
#     }
    
#     # Создаем словарь для хранения выборов игрока
#     player_character = default_character.copy()


#     screen character_creation():
#     modal True
    
#     frame:
#         xfill True
#         yfill True
        
#         vbox:
#             spacing 20
#             xalign 0.5
#             yalign 0.5
            
#             text "Character Creation" size 40 xalign 0.5
            
#             # Имя персонажа
#             vbox:
#                 text "Name:"
#                 input default "" value ScreenVariableInputValue("player_character['name']")
            
#             # Выбор пола
#             vbox:
#                 text "Gender:"
#                 hbox:
#                     textbutton "Male" action SetDict(player_character, "gender", "male")
#                     textbutton "Female" action SetDict(player_character, "gender", "female")
            
#             # Выбор цвета волос
#             vbox:
#                 text "Hair Color:"
#                 hbox:
#                     for color in ["brown", "black", "blonde", "red"]:
#                         textbutton color action SetDict(player_character, "hair_color", color)
            
#             # Выбор цвета глаз
#             vbox:
#                 text "Eye Color:"
#                 hbox:
#                     for color in ["blue", "green", "brown", "gray"]:
#                         textbutton color action SetDict(player_character, "eye_color", color)
            
#             # Выбор одежды
#             vbox:
#                 text "Outfit:"
#                 hbox:
#                     for outfit in ["casual", "formal", "sporty"]:
#                         textbutton outfit action SetDict(player_character, "outfit", outfit)
            
#             # Предпросмотр персонажа
#             frame:
#                 xsize 300
#                 ysize 400
#                 xalign 0.5
                
#                 add "character_preview" # Здесь должно быть изображение персонажа
            
#             # Кнопки управления
#             hbox:
#                 spacing 20
#                 xalign 0.5
#                 textbutton "Reset" action SetVariable("player_character", default_character.copy())
#                 textbutton "Confirm" action Return()


#     label start:

#     scene bg room

#     #     # Вставка значения х в строку
#     #     # e "Красава дай [x]" 

#     #     e "О, ты из клана [mc_bruha.clan]"
#     #     e "У тебя сила [mc_bruha.params['strength']], знание [mc_bruha.skills['knowledge']], дисциплина [mc_bruha.disc['power']]"
#     #     $ check(mc_bruha.params['strength'], 0, mc_bruha.skills['knowledge'], mc_bruha.disc['power'])
#     #     e "Итого [quantityDices] d6. Бросок [result] -> Успехов [successes]"

#     #     jump start

#     #     return



#     # scene bg room
    
#     show lsf
#     # e "Где-то здесь должен быть чарник"

#     return
# }

# Вы можете расположить сценарий своей игры в этом файле.
init python:
    from characterClass import MainCharacter
    import itertools
# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

default bruha = MainCharacter("Томас", "Бруха", 13, {"Могущество":1, "Стойкость":1, "Стремительность":1})
define VHBOX_TEXT_WIDTH = 320

# Игра начинается здесь:
label start:
    # Стили для точек
    style dot_button:
        # background "#666666"
        # hover_background "#888888"
        # selected_background "#ff4444"
        font "fonts/VTMB_MainFont3_0.ttf"  # Путь к вашему шрифту

        background "images/empty.jpeg"
        hover_background "images/hover.jpeg"
        selected_background "images/selected.jpeg"

        xminimum 20
        yminimum 20
        xmaximum 20
        ymaximum 20
        ypos 10
        xpos 20
        margin (0, 0, 0, )
    style vtm_font:
        font "fonts/VTMB_MainFont3_0.ttf"  # Путь к вашему шрифту
        color "#947956"
        size 30

    style vtm_font_headers:
        font "fonts/VTMB_MainFont3_0.ttf"  # Путь к вашему шрифту
        color "#fdf6c2"
        size 40

    # Определение экрана листа персонажа
    screen character_sheet():
        modal True

        frame:
            xfill True
            yfill True
            style_prefix "character_sheet"

            vbox:
                spacing 20
                # Имя клан поколение
                hbox:
                    spacing 20
                    text "Имя: [bruha.name]" size 30 style "vtm_font_headers"
                    text "Клан: [bruha.clan]" size 30 style "vtm_font_headers"
                    text "Поколение: [bruha.generation]" size 30 style "vtm_font_headers"

                # Заголовок Атрибутов
                text "Атрибуты" xalign 0.5 style "vtm_font_headers"

                hbox:
                    spacing 50
                    for i in range(3):
                        vbox:
                            if i == 0:
                                text "Физические" xalign 0.5 style "vtm_font_headers"
                            elif i == 1:
                                text "Социальные" xalign 0.5 style "vtm_font_headers"
                            elif i == 2:
                                text "Ментальные" xalign 0.5 style "vtm_font_headers"
                            for attr, value in itertools.islice(bruha.attributes.items(), 0 + 3 * i, 3 + 3 * i):
                                hbox:
                                    text "[attr]" min_width VHBOX_TEXT_WIDTH style "vtm_font"
                                    hbox:
                                        spacing 5
                                        for i in range(5):  # максимум 5 точек
                                            button:
                                                style "dot_button"
                                                selected i < value
                                                action SetDict(bruha.attributes, attr, i + 1)

                text "Умения" xalign 0.5 style "vtm_font_headers"

                hbox:
                    spacing 50
                    for i in range(3):
                        vbox:
                            if i == 0:
                                text "Таланты" xalign 0.5 style "vtm_font_headers"
                            elif i == 1:
                                text "Навыки" xalign 0.5 style "vtm_font_headers"
                            elif i == 2:
                                text "Знания" xalign 0.5 style "vtm_font_headers"
                            for attr, value in itertools.islice(bruha.skills.items(), 0 + 4 * i, 4 + 4 * i):
                                hbox:
                                    text "[attr]" min_width VHBOX_TEXT_WIDTH style "vtm_font"
                                    hbox:
                                        spacing 5
                                        for i in range(5):
                                            button:
                                                style "dot_button"
                                                selected i < value
                                                action SetDict(bruha.skills, attr, i + 1)

                text "Дисциплины" xalign 0.5 style "vtm_font_headers"

                hbox:
                    spacing 50

                    for attr, value in bruha.disciplines.items():
                        hbox:
                            text "[attr]" min_width VHBOX_TEXT_WIDTH style "vtm_font"
                            hbox:
                                spacing 5
                                for i in range(5):
                                    button:
                                        style "dot_button"
                                        selected i < value
                                        action SetDict(bruha.disciplines, attr, i + 1)
                                        
                # textbutton "Сохранить" action save(bruha)
                # textbutton "Закрыть" action Hide("character_sheet")
                textbutton "Закрыть" action Return()
    
    call screen character_sheet
    jump testlb

label testlb:
    e "сила [bruha.attributes['Сила']], Ловкость [bruha.attributes['Ловкость']], Выносливость [bruha.attributes['Выносливость']], Харизма [bruha.attributes['Харизма']], Манипулирование [bruha.attributes['Манипулирование']], Внешность [bruha.attributes['Внешность']]
    Внимательность [bruha.attributes['Внимательность']], Интеллект [bruha.attributes['Интеллект']], Смекалка [bruha.attributes['Смекалка']], Борьба [bruha.skills['Борьба']] Уклонение [bruha.skills['Уклонение']], Устрашение [bruha.skills['Устрашение']]
    Интриганство [bruha.skills['Интриганство']] ,Стрельба [bruha.skills['Стрельба']], Холодное оружие [bruha.skills['Холодное оружие']], Безопасность [bruha.skills['Безопасность']], Скрытность [bruha.skills['Скрытность']], Компьютеры [bruha.skills['Компьютеры']]"
    e "Финансы [bruha.skills['Финансы']], Финансы [bruha.skills['Финансы']], Обыск [bruha.skills['Обыск']], Ученость [bruha.skills['Ученость']], Могущество [bruha.disciplines['Могущество']], Стойкость [bruha.disciplines['Стойкость']],
    Стремительность [bruha.disciplines['Стремительность']],"

