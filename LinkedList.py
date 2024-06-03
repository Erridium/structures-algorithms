'''
    =[ Связный список ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
'''
    создаем класс "Узел"
    который хранит некоторую информацию в переменной data
    а в переменной next хранит ссылку на следубщий элемент списка 
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

'''
    создаем класс "Связный Список"
    он имеет следующие методы
'''
class LinkedList:
    '''
        ссылка на начало списка
        переменная head определяется
        при создании экземпляра списка
    '''
    def __init__(self):
        self.head = None

    '''
        метод добавления узла
    '''
    def append(self, data):
        new_node = Node(data) # Создаем новый узел
        if self.head is None: # Если у нас "пустая" голова (то есть у нас еще нет элементов)
            self.head = new_node # называем текущий узел головой
            return
        last_node = self.head # устанавливаем "указатель" последнего элемента на голову
        while last_node.next: # пока существует следующий узел
            last_node = last_node.next # перемещаем "узказатель" на следующий элемент
        last_node.next = new_node # у последнего элемента создаем ссылку на новый узел

    '''
        метод удаления узла
    '''
    def remove(self, key):
        current_node = self.head
        # если мы удаляем голову, то в качестве головы нужно назначить следующий за ней узел
        if current_node is not None and current_node.data == key: 
            self.head = current_node.next
            current_node = None
            return

        # если элемент находится не в начале или середине списка, то мы ищем удаляемый элемент
        prev = None
        while current_node is not None and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # если мы дошли до конца списка, то выходим из метода
        if current_node is None:
            return

        # записываем предыдущему элементу ссылку на следующий, удаляем искомый
        prev.next = current_node.next
        current_node = None

    '''
        метод выводит все элементы списка
    '''
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=", ")
            current_node = current_node.next
        print()

'''
    Пример использования
'''
if __name__ == "__main__":
    linked_list = LinkedList() # создаем список
    linked_list.append('a') # добавляем буквы
    linked_list.append('b')
    linked_list.append('c')
    for i in range(10): # добавляем 10 цифр
        linked_list.append(i)

    # посмотрим что в списке
    print("После добавления элементов в список")
    linked_list.print_list()

    linked_list.remove('a') # удаляем голову
    linked_list.remove(0) # удаляем из середины списка
    linked_list.remove(9) # удаляем с конца списка

    # посмотрим что в списке
    print("После удаления элементов из списка")
    linked_list.print_list()
