"""
5. (1) Запросите у пользователя значения выручки и издержек фирмы.
   (2) Определите, с каким финансовым результатом работает фирма
       (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
   (3) Выведите соответствующее сообщение.
   (4) Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
   (5) Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
# (1) Запросите у пользователя значения выручки и издержек фирмы.
revenue = abs(int(input("Введите значение выручки фирмы :\n")))
costs = abs(int(input("Введите значение издержек фирмы :\n")))

# (2) Определите, с каким финансовым результатом работает фирма
#     (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
profit = revenue - costs
if profit < 0:

# (3) Выведите соответствующее сообщение.
   print("Деятельность фирмы убыточна (издержки больше выручки), убыток составляет: \n", profit)
else:

# (3) Выведите соответствующее сообщение.
   print("Деятельность фирмы прибыльна (выручка больше издержек), прибыль составляет: \n", profit)

# (4) Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
   print("Рентабельность выручки (соотношение прибыли к выручке) составляет: \n", profit/revenue)

# (5) Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
   workers = abs(int(input("Введите численность сотрудников фирмы :\n")))
   print("Прибыль фирмы в расчете на одного сотрудника составляет: \n", profit/workers)

