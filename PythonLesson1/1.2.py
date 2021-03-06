"""
2. (1) Пользователь вводит время в секундах.
   (2) Переведите время в часы, минуты и секунды и
   (3) выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
# (1) Пользователь вводит время в секундах.
input_seconds = int(input("Введите время в секундах (целое число):"))

# (2) Переведите время в часы, минуты и секунды
# в часе 3600 скекунд, в минуте 60 секунд

days = input_seconds // (3600*24)
hours = (input_seconds - days*3600*24)// 3600
minutes = (input_seconds - days*3600*24 - hours * 3600) // 60
seconds = input_seconds - days*3600*24 - hours * 3600 - minutes * 60

# (3) выведите в формате чч:мм:сс. Используйте форматирование строк.
if input_seconds <= (3600*23+59*60+59):
    print(f"{hours:2}:{minutes:2}:{seconds:2}")
else:
    print("Введеное количество секунд эквивалентно:\n", days, " дней\n", f"{hours:2}:{minutes:2}:{seconds:2}")