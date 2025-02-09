# Вы можете расположить сценарий своей игры в этом файле.
init python:
    from characterClass import MainCharacter
    import itertools

    def check_points(attributes, attr, i):
        global points
        if points > 0:
            if attributes[attr] < i:
                points -= 1
                return True
            else:
                return False
        # global points
        # if points != 0:
        #     points -= 1
        #     return True
        # else:
        #     return False

    def setDictMy(attributes, attr, i):
        global points
        if points > 0:
            if attributes[attr] < i:
                points -= 1
                attributes[attr] += 1
                return True
            else:
                return False
        

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

default bruha = MainCharacter("", "Бруха", 13, {"Могущество":1, "Стойкость":1, "Стремительность":1})
define VHBOX_TEXT_WIDTH = 320
default points = 5

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

    style vtm_font_clans:
        font "fonts/VTMB_MainFont3_0.ttf"  # Путь к вашему шрифту
        color "#fdf6c2"
        hover_color "#99904f"
        selected_color "#db3a3a"
        size 30

    style vtm_clan_info:
        font "fonts/VTMB_MainFont3_0.ttf"  # Путь к вашему шрифту
        color "#fdf6c2"
        justify True
        xsize 1000
        size 30


    # меню выбора клана
    screen clan_choose:
        vbox:
            xpos 20
            button: # 1
                hbox:
                    spacing 10
                    add "images/bruha_clan_image.jpg":
                        size (50, 50)
                    text "Бруха" style "vtm_font_clans"
                # idle_background при наведении картинка исчезает
                # hover_background при наведении картинка появляется
                # selected_background при выборе картинка появляется
                # insensitive_background при хуй знает чем, хуй знает что
                action ToggleScreen("bruha_clan_info")
        # vbox: эта строка лишняя, УБРАТЬ ЕСЛИ СОБИРАЕШЬСЯ расскоментировать  ВСЕ КЛАНЫ
            # textbutton "Гангрел": # 2
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Носферату": # 3
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Тремор": # 4
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Малкавианен": # 5
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Тореадор": # 6
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Вентру": # 7
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Сетиты": # 8
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Цимисхи": # 9
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Ласомбра": # 10
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Равнос": # 11
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Ассамиты": # 12
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Джованни": # 13
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 
            # textbutton "Clan": 
            #     text_style "vtm_font_headers"
            #     action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")] 

    screen bruha_clan_info:
        hbox:
            xalign 0.2
            xsize 1000
            ypos -20
            viewport:
                mousewheel True
                draggable True
                text """
                    Клан Бруха в основном состоит из бунтарей, как идейных,
                так и безыдейных. Индивидуалистичные, искренние и буйные, Бруха 
                придают огромное значение социальным изменениям, и среди 
                представителей клана имеются некоторые из наиболее жестоких 
                Сородичей Камарильи. Большинство прочих вампиров считают Бруха 
                не более чем бандитами и негодяями, но истина в том, что 
                подлинная страсть лежит за пределами досягаемости подобных 
                обвинений. Сородичи Бруха лелеют любимые страсти и цели, которые 
                защищают с силой и яростью. Некоторые Бруха следуют за 
                обаятельными представителями своего клана, в то время как другие
                предпочитают позицию вопиющего, вызывающего индивидуализма.
                    У клана богатая история, в которой было множество поэтов–
                воинов, и он сохранил эту концепцию и в нынешние ночи; многим 
                Бруха нравится высказать свою идею, а затем отдаться порыву 
                разрушения, чтобы проиллюстрировать свою точку зрения. Любовь 
                Сброда к переменам объединяет их, путь и непрочно, в еженощных 
                крестовых походах. При появлении общего врага Бруха со 
                значительно отличающимися идеалами объединятся, чтобы вместе 
                противостоять недругу. Однако, после того как враг повержен, все 
                обязательства отзываются и дело идёт дальше, как обычно.
                    Распространённая идея Бруха связана с созданием вампирской 
                «Утопии» или воссозданием мифической, уже существовавшей в былые 
                ночи, — хотя у каждого Бруха имеется собственное мнение о том, 
                чем же является эта Утопия. Для внедрения своих идей Бруха 
                полагаются на хаос и перевороты, и для Сброда допустима 
                определённая свобода действий, которой нет у других кланов. По 
                сути, от Бруха почти ожидают, что они будут непредсказуемыми и 
                агрессивными; этот стереотип с пользой используется многими 
                убедительными и красноречивыми представителям клана, которым 
                необходимо прибегать к насилию при продвижении своих аргументов. 
                Уважаемые за свои боевые качества и готовность встать под знамя, 
                Бруха — это физическая сила Камарильи. Однако в последнее время 
                многие неонаты Бруха начали считать, что их роль в Камарилье — 
                создание собственной организации, и в клане начались немалые 
                беспокойства. Другие Сородичи полагают, что Бруха первыми 
                покинут Камарилью. Сами Бруха тоже верят в это…""" style "vtm_clan_info"
            add "images/Bruha.jpg":
                xpos 10
                size (400, 600)

    # Определение экрана листа персонажа


    screen character_sheet():
        modal True

        frame:
            xfill True
            yfill True
            style_prefix "character_sheet"

            vbox:
                xpos 20
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
                    # text "Клан: [bruha.clan]" size 30 style "vtm_font_headers"


                    textbutton "Выбрать клан   ":
                        ypos -6
                        text_style "vtm_font_headers"
                        action [ToggleScreen("clan_choose"), ToggleScreen("character_sheet")]



                    text "Поколение: [bruha.generation]" size 30 style "vtm_font_headers"
                
                # Заголовок Атрибутов
                text "Атрибуты" xalign 0.5 style "vtm_font_headers"

                hbox:
                    spacing 50
                    for i in range(3):
                        vbox:
                            if i == 0:
                                text "Физические [points]" xalign 0.5 style "vtm_font_headers"
                            elif i == 1:
                                text "Социальные [points]" xalign 0.5 style "vtm_font_headers"
                            elif i == 2:
                                text "Ментальные [points]" xalign 0.5 style "vtm_font_headers"
                            for attr, value in itertools.islice(bruha.attributes.items(), 0 + 3 * i, 3 + 3 * i):
                                hbox:
                                    text "[attr]" min_width VHBOX_TEXT_WIDTH style "vtm_font"
                                    hbox:
                                        spacing 5
                                        for i in range(5):  # максимум 5 точек
                                            button:
                                                style "dot_button"
                                                selected i < value
                                                # sensitive(points > 3)

                                                # action If(check_points(bruha.attributes, attr, i + 1),
                                                # true=SetDict(bruha.attributes, attr, i + 1))

                                                action If( i + 1 > bruha.attributes[attr], 
                                                [SetVariable("points", points-1), SetDict(bruha.attributes, attr, i + 1)], 
                                                If(i + 1 < bruha.attributes[attr],
                                                [SetVariable("points", points+1), SetDict(bruha.attributes, attr, i + 1)]))

                                                # action setDictMy(bruha.attributes, attr, i + 1)

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
    
    define points = 5
    call screen character_sheet
    # call screen clan_choose

    jump testlb

label testlb:
    e "сила [bruha.attributes['Сила']], Ловкость [bruha.attributes['Ловкость']], Выносливость [bruha.attributes['Выносливость']], Харизма [bruha.attributes['Харизма']], Манипулирование [bruha.attributes['Манипулирование']], Внешность [bruha.attributes['Внешность']]
    Внимательность [bruha.attributes['Внимательность']], Интеллект [bruha.attributes['Интеллект']], Смекалка [bruha.attributes['Смекалка']], Борьба [bruha.skills['Борьба']] Уклонение [bruha.skills['Уклонение']], Устрашение [bruha.skills['Устрашение']]
    Интриганство [bruha.skills['Интриганство']] ,Стрельба [bruha.skills['Стрельба']], Холодное оружие [bruha.skills['Холодное оружие']], Безопасность [bruha.skills['Безопасность']], Скрытность [bruha.skills['Скрытность']], Компьютеры [bruha.skills['Компьютеры']]"
    e "Финансы [bruha.skills['Финансы']], Финансы [bruha.skills['Финансы']], Обыск [bruha.skills['Обыск']], Ученость [bruha.skills['Ученость']], Могущество [bruha.disciplines['Могущество']], Стойкость [bruha.disciplines['Стойкость']],
    Стремительность [bruha.disciplines['Стремительность']], имя [bruha.name]"

