'''
    =[ Множества ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
class Set: # создаем класс множества
    def __init__(self, elements=None):  #  инициализируем множество
        self.data = {}
        if elements:
            for element in elements:
                self.add(element)

    def add(self, element):  # доьавляем в множество жлементы
        self.data[element] = True

    def remove(self, element):  # удаляем элементы из множества
        if element in self.data:
            del self.data[element]

    def contains(self, element): # проверка, содержит ли множество данный элемент
        return element in self.data

    def union(self, other_set): # объеданение множеств
        result = Set()
        for element in self.data:
            result.add(element)
        for element in other_set.data:
            result.add(element)
        return result

    def intersection(self, other_set): # поиск пересечений множеств
        result = Set()
        for element in self.data:
            if element in other_set.data:
                result.add(element)
        return result

    def difference(self, other_set): # поиск различий между множествами
        result = Set()
        for element in self.data:
            if element not in other_set.data:
                result.add(element)
        return result

    def is_subset(self, other_set): # проверка подмножества
        for element in self.data:
            if element not in other_set.data:
                return False
        return True

    def __len__(self):  # размер множества
        return len(self.data)

    def __str__(self): # преобразование мнжества в строку для вывода
        return "{" + ", ".join(str(x) for x in self.data) + "}"


# Пример использования
if __name__ == "__main__":
    my_set = Set([1, 2, 3, 4, 5])  # создаем множество из 5 цифр
    print(my_set)  # вывод: {1, 2, 3, 4, 5}
    
    my_set.add(6)  #  добавляем 6
    print(my_set)  # вывод: {1, 2, 3, 4, 5, 6}
    
    my_set.remove(3)  # удаляем 3
    print(my_set)  # вывод: {1, 2, 4, 5, 6}
    
     # проверяем содердит ли мноджество числа 4 и 3
    print(my_set.contains(4))  # вывод: True
    print(my_set.contains(3))  # вывод: False
    
    other_set = Set([4, 5, 6, 7, 8])  #  создаем еще 1 множество
    union_set = my_set.union(other_set)  # объединяем множества
    print(union_set)  # вывод: {1, 2, 4, 5, 6, 7, 8}
    
    intersection_set = my_set.intersection(other_set)  # пересечение множеств
    print(intersection_set)  # вывод: {4, 5, 6}
    
    difference_set = my_set.difference(other_set)  #  разница множеств
    print(difference_set)  # вывод: {1, 2}
    
     #  является ли множество подмножеством
    print(my_set.is_subset(union_set))  # вывод: True
    print(union_set.is_subset(my_set))  # вывод: False
    
     # длина множетсва
    print(len(my_set))  # вывод: 5
