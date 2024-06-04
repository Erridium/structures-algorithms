'''
    =[ Стек (стопка) ]=
    
    Работу выполнил - Мищенко И.Р.
    Группа - 2Б
'''
class Node: # создаем класс - узел дерева
    def __init__(self, data):
        self.data = data # данные  
        self.left = None # левый
        self.right = None# правый соседи

class BinaryTree:
    def __init__(self): # корень 
        self.root = None

    def insert(self, data): # вставка нового узла
        new_node = Node(data)
        if self.root is None: # Если это первый узел, делаем его корневым
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data: # если новое число меньше настоящего, заполняем левуб ветку
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else: # иначе заполняем правую ветку
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def in_order_traversal(self, node): # вывод в порядке возрастания
        if node:
            self.in_order_traversal(node.left) # сначала издалека левая ветка
            print(node.data, end=' ')
            self.in_order_traversal(node.right) # потом от корня правая ветка

    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=' ')
            self.pre_order_traversal(node.left) # сначала от корня левая ветка
            self.pre_order_traversal(node.right) # потом от корня правая ветка

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left) # сначала издалека левая ветка
            self.post_order_traversal(node.right) # потом издалека правая ветка
            print(node.data, end=' ')
    
    def delete(self, data):
        self.root = self.delete_node(self.root, data)

    '''
    Если узел является листовым (у него нет потомков), он просто удаляется.
    Если у узла есть только один потомок, этот потомок становится новым корнем поддерева.
    Если у узла есть два потомка, мы находим минимальное значение в правом поддереве и заменяем им значение удаляемого узла, а затем рекурсивно удаляем этот минимальный узел.
    '''
    def delete_node(self, node, data):
        if node is None: # если узел пустой, возвращаемся назад
            return node

        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.data = self.min_value(node.right)
            node.right = self.delete_node(node.right, node.data)

        return node

    def min_value(self, node): # ищем минимальное значение
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.data


# Пример использования
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5) # заполняем дерево
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(7)
    tree.insert(2)
    tree.insert(6)
    tree.insert(8)
    
    # Выводим дерево разными способами
    print("In-order:")
    tree.in_order_traversal(tree.root)
    print("\n\nPre-order:")
    tree.pre_order_traversal(tree.root)
    print("\n\nPost-order:")
    tree.post_order_traversal(tree.root)
    
    tree.delete(5)
    tree.delete(3)
    tree.delete(8)
    print("\n\nОбход In-order после удаления '5', '3', '8':")
    tree.in_order_traversal(tree.root)
    print()
