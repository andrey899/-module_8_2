
 #Задача "План перехват".

# Функция personal_sum(numbers) принимает коллекцию numbers.
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            # Подсчитывает сумму чисел в numbers путём перебора и увеличивает переменную result.
            result += i
        except TypeError:
            # Если же при переборе встречаются данные типа отличного от числового,
            # то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")

    # Функция возвращает кортеж из двух значений:
    # result - сумма чисел, incorrect_data - кол-во некорректных данных.
    return result, incorrect_data


# Функция calculate_average(numbers) принимает коллекцию numbers и возвращает: среднее арифметическое всех чисел.
def calculate_average(numbers):
    """ Функция подсчитывает среднее арифметическое чисел в коллекции numbers.
    В случае пустой коллекции возвращает 0.
    В случае некорректного типа данных в numbers возвращает None и выводит сообщение об ошибке."""
    try:
        # Внутри calculate_average(numbers) для подсчёта суммы используйте функцию personal_sum.
        total, incorrect_data = personal_sum(numbers)
        # Количество чисел в numbers без учёта некорректных данных.
        count = len(numbers) - incorrect_data
        # Функция calculate_average(numbers) возвращает: среднее арифметическое всех чисел -
        # сумма чисел total делённая на их количество count. Если чисел 0 возвращает 0.
        return total / count if count != 0 else 0
    except ZeroDivisionError:
        # Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError
        # при делении на 0 и верните 0.
        return 0
    except TypeError:
        # Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
        # Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
        print('В numbers записан некорректный тип данных')
        # В таком случае функция просто вернёт None.
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать