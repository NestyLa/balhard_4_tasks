"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Что за планета?
Нужно отредактировать функцию get_planet_name, которая принимает номер планеты
так, чтобы она возвращала название планеты

Планеты в порядке их удаления от слонца:
1) Меркурий
2) Венера
3) Земля
4) Марс
5) Юпитер
6) Сатурн
7) Уран
8) Нептун

ПРИМЕРЫ
--------------------------------------------------------------------------------
get_planet_name(3) -> 'Земля'
"""


def get_planet_name(planet_num: int) -> str:
    planets_of_suns_system = {1: 'Меркурий', 2: "Венера", 3: 'Земля', 4: 'Марс',
                              5: 'Юпитер', 6: 'Сатурн', 7: 'Уран', 8: 'Нептун'
                              }
    result = planets_of_suns_system.get(planet_num)
    return result


if __name__ != '__main__':
    pass
else:
    planet = int(input('Введите номер планеты: '))
    print(f'Планета: {get_planet_name(planet)}')
