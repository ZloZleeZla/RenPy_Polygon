# Класс главного персонажа
class MainCharacter():
    # init вызывается при создании экземпляра класса
    def __init__(self, clan, params, skills, disciplines):
        self.clan = clan
        self.params = params  # Параметры
        self.skills = skills  # Навыки
        self.disc = disciplines  # Дисциплины


# Параметры, навыки и дисциплины представляются в виде словарей
# params = {"strength": 4, "intellect": 1}
# skills = {"brawler": 3, "fighting": 5, "knowledge": 1}
# disciplines = {"power": 3, "resistance": 2}
# bruha = MainCharacter(clan="Бруха", params=params,
#                       skills=skills, disciplines=disciplines)


# print(dir(bruha))
# print(bruha.clan)
# print(bruha.params["strength"])
# print(bruha.disc["power"])
