import itertools

skills = {
    "Борьба": 1,
    "Уклонение": 1,
    "Устрашение": 1,
    "Интриганство": 1,
    "Стрельба": 1,
    "Холодное оружие": 1,
    "Безопасность": 1,
    "Скрытность": 1,
    "Компьютеры": 1,
    "Финансы": 1,
    "Обыск": 1,
    "Ученость": 1
}
for i in range(3):
    print(i)
    for attr, value in itertools.islice(skills.items(), 0 + 4 * i, 4 + 4 * i):
        print(f"{attr} {value}")
