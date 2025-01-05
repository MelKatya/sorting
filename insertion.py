from typing import List, Union
from timer_dec import timer


@timer
def insertion_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Сортировка списка вставками
    Алгоритм проходит по списку, начиная со второго элемента,
    и вставляет текущий элемент в его корректное место среди уже
    отсортированных элементов.
    """
    sorted_numbers = numbers[:]

    for i in range(1, len(sorted_numbers)):
        # Сохраняем текущее значение и индекс
        value = sorted_numbers[i]
        index = i

        # Перемещаем элементы, которые больше текущего значения, на позицию вперед
        while index > 0 and sorted_numbers[index - 1] > value:
            sorted_numbers[index] = sorted_numbers[index - 1]
            index -= 1

        # Вставляем текущее значение на правильную позицию
        sorted_numbers[index] = value

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = insertion_sort(numbers_list)
print(result_1)
print()
