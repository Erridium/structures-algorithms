'''
    =[ Очередь ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
class Node: # создаем класс "Узел"
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue: # создаем класс "Очередь"
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self): # проверка: если начало пустое, значит очередь пуста
        return self.front is None

    def enqueue(self, item): # Добавляем элемент в конец очереди
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self): # Забираем элемент из очереди 
        if self.is_empty(): # проверка что очередь не пуста
            return None
        else:
            dequeued_item = self.front.data # забираем данные
            self.front = self.front.next # Удаляем элемент
            if self.front is None: 
                self.rear = None
            return dequeued_item

    def peek(self): # Спросим какой элемент находится в начале очереди
        if self.is_empty(): # проверка что очередь не пуста
            return None
        else:
            return self.front.data

    def size(self): # Длина очереди
        count = 0
        current = self.front # идем сначала в конец и считаем
        while current is not None: 
            count += 1
            current = current.next
        return count

# Пример использования
if __name__ == "__main__":
    queue = Queue()                                 # Создаем объект
    print(f"До заполнения:\
                    {queue.is_empty() = }") # Вывод: True 
    for i in ['A','B','C','D','E']:                 # Заполняем очередь
        queue.enqueue(i)
    print(f"После заполнения:\
                  {queue.is_empty() = }") # Вывод: False 
    
    print(f"Забираем из очереди 1-й элемент:\
    {queue.dequeue() = }")  # Вывод: A
    print(f"Смотрим какой сейчас 1-й элемент:\
    {queue.peek() = }")     # Вывод: B
    print(f"Длина очереди:\
                        {queue.size() = }")     # Вывод: 4
