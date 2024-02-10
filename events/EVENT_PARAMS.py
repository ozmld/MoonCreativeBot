KARAOKE_DESCRIPTION = """
Имеете крутой скилл пения или хотите попробовать что-то новое для себя? Тогда присоединяйтесь на событие караоке!

Вы не только отлично проведете время, но и покажете все свои возможности другим.
"""

ANIME_DESCRIPTION = """
Награда за озвучку 1 серии - 50 мункоинов

Станьте реальными героями аниме и опробуйте себя в озвучивании!

Невероятная атмосфера, веселое времяпровождение обеспечено, поэтому покажите свой перфоманс остальным.
"""

FILM_DESCRIPTION = """
Награда за просмотр - 200 мункоинов
"""

HORROR_DESCRIPTION = """
Награда за просмотр - 100 мункоинов

Выключайте весь свет дома и самое главное, не оборачивайтесь...  Пришло время для страшных историй!

А если вы являетесь ценителем хоррора, то не пропустите наш ивент и проверьте свою выносливость.
"""

EVENTS_DECRIPTION = {
    "Караоке": KARAOKE_DESCRIPTION,
    "Озвучка": ANIME_DESCRIPTION,
    "Кино": FILM_DESCRIPTION,
    "Хоррор": HORROR_DESCRIPTION,
}

with open('./events/EVENTS_BYTES/KARAOKE_BYTES.txt', 'rb') as f:
    KARAOKE_BYTES = f.read()

with open('./events/EVENTS_BYTES/ANIME_BYTES.txt', 'rb') as f:
    ANIME_BYTES = f.read()

with open('./events/EVENTS_BYTES/FILM_BYTES.txt', 'rb') as f:
    FILM_BYTES = f.read()

with open('./events/EVENTS_BYTES/HORROR_BYTES.txt', 'rb') as f:
    HORROR_BYTES = f.read()

EVENTS_IMAGES = {
    "Караоке": KARAOKE_BYTES,
    "Озвучка": ANIME_BYTES,
    "Кино": FILM_BYTES,
    "Хоррор": HORROR_BYTES,
}
