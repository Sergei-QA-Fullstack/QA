# Напишите программу, которая:
#
# 1. Спрашивает у пользователя год его рождения.
# 2. Рассчитывает возраст пользователя.
# 3. В зависимости от возраста выводит:


def age_message():
    data_of_birth=int(input("Введите год вашего рождения: "))
    age=2025-data_of_birth
    print(f"Ваш возраст = {age}")
    if age < 0:
        print("Ошибка, вам не может быть меньше 0 лет")
    elif age<18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif age>=18 and age<65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

age_message()