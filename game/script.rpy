# Вы можете расположить сценарий своей игры в этом файле.
init python:
    from characterClass import MainCharacter
    import itertools


# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

default bruha = MainCharacter("", "Бруха", 13, {"Могущество":1, "Стойкость":1, "Стремительность":1})
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
        size 30


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
                    # text "Имя: [bruha.name]" size 30 style "vtm_font_headers"
                    text "Имя:" size 30 style "vtm_font_headers"# Текст слева по умолчанию сука

                    hbox:
                        xsize 180
                        input:
                            id "nameInput"
                            style "vtm_font_headers"
                            value FieldInputValue(bruha, 'name')  # Привязка к player.name
                            length 10  # Максимальная длина
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
    Стремительность [bruha.disciplines['Стремительность']], имя [bruha.name]"

