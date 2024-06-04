'''
    =[ Стек (стопка) ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
class Node: # создаем класс "Узел"
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack: # Создаем класс "стопка"
    def __init__(self):
        self.top = None

    def push(self, item): # добавляем новый узел
        new_node = Node(item)
        new_node.prev = self.top
        self.top = new_node

    def pop(self): # изымаем последний элемент из стопки
        if self.is_empty(): # проверяем что стопка не пуста
            raise IndexError("Stack is empty")
        data = self.top.data  # достаем данные и удаляем узел
        self.top = self.top.prev
        return data

    def peek(self): # смотрим последний элемент из стопки
        if self.is_empty(): # проверяем что стопка не пуста
            raise IndexError("Stack is empty")
        return self.top.data # достаем данные

    def is_empty(self): # просто проверяем не пуста ли стопка
        return self.top is None

    def __len__(self): # считаем "высоту" стопки
        count = 0
        current = self.top # начинаем сверху
        while current:
            count += 1 # и идем вниз
            current = current.prev
        return count

# Пример использования
if __name__ == "__main__":
    stack = Stack()
    print(f"{stack.is_empty() = }") # Вывод: True 
    for i in ['A','B','C','D','E']: # заполняю стек
        stack.push(i)
    print(f"{stack.pop() = }")      # Вывод: E
    print(f"{stack.peek() = }")     # Вывод: D
    print(f"{len(stack) = }")       # Вывод: 4
    print(f"{stack.is_empty() = }") # Вывод: False 
