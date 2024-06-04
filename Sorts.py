'''
    =[ Сортировки ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
import random
import time
'''
Сортировка пузырьком - простой алгоритм, но имеет высокую временную сложность O(n^2),
поэтому не очень эффективен для больших списков.
'''
def bubble_sort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
Сортировка выбором - также имеет временную сложность O(n^2),
но более эффективна, чем пузырьковая сортировка.
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

'''
quicksort - один из самых эффективных алгоритмов сортировки,
имеет среднюю временную сложность O(n log n),
но может иметь худшую сложность O(n^2) в некоторых случаях.
'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# Пример использования
if __name__ == "__main__":
    unsorted_list = list(range(10**4))
    while True:
        random.shuffle(unsorted_list)
        choose = input("\n[Ввод] Выберите алгоритм сортировки (1-bubble/2-selection/3-quick): ")
        start_time = time.time()
        if choose == '1':
            #print(f"{unsorted_list = }")
            sorted_list = bubble_sort(unsorted_list)
            #print(f"{sorted_list = }")
        elif choose == '2':
            #print(f"{unsorted_list = }")
            sorted_list = selection_sort(unsorted_list)
            #print(f"{sorted_list = }")
        elif choose == '3':
            #print(f"{unsorted_list = }")
            sorted_list = quicksort(unsorted_list)
            #print(f"{sorted_list = }")
        else:
            print("[!] Неверный ввод\n")
        print("Время сортировки:", time.time() - start_time)