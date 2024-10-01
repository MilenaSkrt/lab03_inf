def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если элемент найден больше следующего
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел для сортировки: "))

# Запрашиваем числа
numbers = []
for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Сортируем числа
bubble_sort(numbers)

# Выводим отсортированные числа
print("Отсортированные числа:", numbers)
