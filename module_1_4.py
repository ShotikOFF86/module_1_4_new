city = input("Введите город: ")
print("Ваш город, ",city.upper())
print("Ваш город, ",city.replace(" ",""))
print("Ваш город, ",city [:3])
print("Ваш город, ",city [-1])
current_yеar = 2024
year_of_foundation = int(input("Год основания Вашего города "))
age_city = current_yеar - year_of_foundation
print("В этом году Вашему городу ", age_city, "лет")
print("Колличество символов в названии города",len(city))
