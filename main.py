# Задача 1: Укажите, в какой из выборок наибольшее стандартное отклонение

data1 = [1, 3, 2, 4, 5, 7, 1, 8]
data2 = [100, 300,250, 400, 230, 280, 320, 112]
data3 = [15, 10, 13, 7, 28, 31, 20, 32]

def stdev(dataset):
    diffs = 0
    avg = sum(dataset)/len(dataset)
    for i in dataset:
        diffs += (i - avg)**(2)
    return (diffs/(len(dataset)-1))**(0.5)

# print(stdev(data1))
# print(stdev(data2))
# print(stdev(data3))

# Задача 2:
import math


def func(data: str):
    # Разделяем строку и СРАЗУ конвертируем каждый элемент в число
    new_data = [int(x) for x in data.split(',')]

    # Теперь sum() и остальные расчеты будут работать
    mean = sum(new_data) / len(new_data)

    squared_diffs = []
    for x in new_data:  # Итерируемся по списку чисел new_data, а не по строке data
        squared_diffs.append((x - mean) ** 2)

    variance = sum(squared_diffs) / len(new_data)
    std_dev = math.sqrt(variance)

    print("Дисперсия:", variance)
    print("Стандартное отклонение:", std_dev)


data = "1,5,2,7,1,9,3,8,5,9"
# func(data)  # Не забудьте передать аргумент в скобки


# Мой вариант
def Sd(data):
    mean = sum(data) / len(data)
    E_Sd = []
    for num in data:
        E_Sd.append((num - mean)**2)

    # Скобки должны закрывать ВЕСЬ числитель и ВЕСЬ знаменатель перед корнем
    std_dev = (sum(E_Sd) / (len(data) - 1)) ** 0.5
    variance = sum(E_Sd) / len(data)

    print("Стандартное отклонение:", std_dev)
    print("Дисперсия:", variance)

# Проверка на твоих числах



Sd([1, 5, 2, 7, 1, 9, 3, 8, 5, 9])