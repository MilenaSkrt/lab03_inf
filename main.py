def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если элемент найден больше следующего (или меньше, в зависимости от направления сортировки)
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел для сортировки: "))

# Запрашиваем числа
numbers = []
for i in range(n):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Запрашиваем направление сортировки
direction = input("Введите направление сортировки (введите 'возраст' для сортировки по возрастанию или 'убывание' для сортировки по убыванию): ").strip().lower()
ascending = True if direction == 'возраст' else False if direction == 'убывание' else None

# Проверка на корректность ввода направления сортировки
if ascending is None:
    print("Неверный ввод направления сортировки. Используется сортировка по возрастанию по умолчанию.")
    ascending = True

# Сортируем числа
bubble_sort(numbers, ascending)

# Выводим отсортированные числа
print("Отсортированные числа:", numbers)
