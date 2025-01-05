from typing import List, Union
from timer_dec import timer


@timer
def cocktail_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Сортировка перемешиванием (шейкерная / двунаправленная сортировка).

    Алгоритм проходит по списку в обоих направлениях:
    - В прямом направлении: наибольший элемент перемещается в конец.
    - В обратном направлении: наименьший элемент перемещается в начало.
    Процесс продолжается, пока границы (start и stop) не встретятся.
    """
    sorted_numbers = numbers[:]
    start = 0
    stop = len(sorted_numbers) - 1

    # Выполняем цикл до тех пор, пока границы не пересекутся
    while start < stop:
        # Проходим с слева направо: наибольшее число отправляется в конец
        for i in range(start, stop):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
        # Уменьшаем правую границу
        stop -= 1

        # Проход справа налево: наименьшее число отправляется в начало
        for i in range(stop, start, -1):
            if sorted_numbers[i] < sorted_numbers[i - 1]:
                sorted_numbers[i], sorted_numbers[i - 1] = sorted_numbers[i - 1], sorted_numbers[i]
        # Уменьшаем левую границу
        start += 1

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = cocktail_sort(numbers_list)
print(result_1)
