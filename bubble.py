from typing import List, Union
from timer_dec import timer


@timer
def bubble_sort_classic(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Классическая пузырьковая сортировка.

    Алгоритм проходит по списку несколько раз, сравнивая соседние элементы
    и меняя их местами, если предыдущий элемент больше следующего.
    После каждой итерации наибольший элемент перемещается в конец списка.
    """
    sorted_numbers = numbers[:]

    for i in range(len(sorted_numbers)):
        # Последние i элементов уже отсортированы, их можно пропустить
        for j in range(len(sorted_numbers) - 1 - i):
            # Меняем элементы местами, если они стоят не в порядке возрастания
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

    return sorted_numbers


@timer
def bubble_sort_swapped(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Пузырьковая сортировка с оптимизацией (флаг завершения).

    Алгоритм завершает выполнение раньше, если за проход не было ни одной перестановки,
    что означает, что список уже отсортирован.
    """
    sorted_numbers = numbers[:]
    # Флаг, указывающий, произошли ли перестановки - по умолчанию True
    swapped = True

    while swapped:
        # Сбрасываем флаг перед началом прохода
        swapped = False
        for i in range(len(sorted_numbers) - 1):
            # Меняем элементы местами, если они стоят не в порядке возрастания
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                # Устанавливаем флаг, если была перестановка
                swapped = True

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = bubble_sort_classic(numbers_list)
print(result_1)
print()

result_2 = bubble_sort_swapped(numbers_list)
print(result_2)
