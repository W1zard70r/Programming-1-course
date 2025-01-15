# from natsort import natsorted

# class TreapNode:
#     def __init__(self, key, priority, link):
#         if key is None or priority is None or link is None:
#             raise ValueError("Ключ, приоритет и ссылка не могут быть None")
#         self.key = key
#         self.priority = priority
#         self.link = link
#         self.left = None
#         self.right = None

#     def __repr__(self):
#         return f"TreapNode(key={self.key}, priority={self.priority}, link={self.link})"


# def insert(node, key, priority, link):
#     if node is None:
#         print(f"Вставляем новый узел: key={key}, priority={priority}, link={link}")
#         return TreapNode(key, priority, link)
    
#     print(f"Проверяем узел: {node}")
#     if key == node.key:
#         raise ValueError(f"Ключ {key} уже существует в Treap")
    
#     if key < node.key:
#         print(f"Ищем место в левом поддереве узла {node.key}...")
#         node.left = insert(node.left, key, priority, link)
#         if node.left.priority > node.priority:
#             print(f"Выполняем правую ротацию вокруг узла {node.key}...")
#             node = rotate_right(node)
#     else:
#         print(f"Ищем место в правом поддереве узла {node.key}...")
#         node.right = insert(node.right, key, priority, link)
#         if node.right.priority > node.priority:
#             print(f"Выполняем левую ротацию вокруг узла {node.key}...")
#             node = rotate_left(node)
    
#     return node


# def search_treap(node, key):
#     if node is None:
#         print(f"Узел с ключом {key} не найден.")
#         return None
    
#     print(f"Проверяем узел: {node}")
#     if node.key == key:
#         print(f"Узел найден: {node}")
#         return node
    
#     # Используем естественное сравнение
#     if natsorted([key, node.key])[0] == key:
#         print(f"Ищем в левом поддереве узла {node.key}...")
#         return search_treap(node.left, key)
#     else:
#         print(f"Ищем в правом поддереве узла {node.key}...")
#         return search_treap(node.right, key)


# def rotate_right(node):
#     print(f"Правая ротация вокруг узла {node.key}...")
#     left_child = node.left
#     node.left = left_child.right
#     left_child.right = node
#     return left_child


# def rotate_left(node):
#     print(f"Левая ротация вокруг узла {node.key}...")
#     right_child = node.right
#     node.right = right_child.left
#     right_child.left = node
#     return right_child


# def in_order_traversal(node):
#     if node is not None:
#         in_order_traversal(node.left)
#         print(node)
#         in_order_traversal(node.right)


# def is_treap_valid(node, min_key=None, max_key=None):
#     if node is None:
#         return True
    
#     if (min_key is not None and node.key <= min_key) or (max_key is not None and node.key >= max_key):
#         return False
    
#     if (node.left is not None and node.left.priority > node.priority) or \
#        (node.right is not None and node.right.priority > node.priority):
#         return False
    
#     return is_treap_valid(node.left, min_key, node.key) and is_treap_valid(node.right, node.key, max_key)

class TreapNode:
    def __init__(self, key, priority, link):
        self.key = key  # Ключ для BST
        self.priority = priority  # Приоритет для Heap
        self.link = link # Полный путь до файла
        self.left = None  # Левое поддерево
        self.right = None  # Правое поддерево

class Treap:
    def __init__(self):
        self.root = None  # Корень Treap

def split(root, key):
    """
    Разделяет Treap на два поддерева по ключу.
    """
    if root is None:
        return (None, None)
    if root.key <= key:
        left, right = split(root.right, key)
        root.right = left
        return (root, right)
    else:
        left, right = split(root.left, key)
        root.left = right
        return (left, root)

def merge(left, right):
    """
    Объединяет два Treap в один.
    """
    if left is None:
        return right
    if right is None:
        return left
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right

def insert(treap, key, priority, link):
    
    """
    Вставляет новый узел в Treap.
    Если приоритет не указан, он генерируется случайно.
    """

    new_node = TreapNode(key, priority, link)

    if treap.root is None:
        treap.root = new_node
        return
    
    left, right = split(treap.root, key)
    treap.root = merge(merge(left, new_node), right)

def search_treap(treap, key):
    """
    Поиск узла по ключу.
    Возвращает True, если ключ найден, иначе False.
    """
    return _search(treap.root, key)

def _search(root, key):
    """
    Вспомогательная функция для поиска.
    """
    if root is None:
        return None
    if root.key == key:
        return root
    if key < root.key:
        return _search(root.left, key)
    else:
        return _search(root.right, key)

def inorder(treap):
    """
    Обход дерева в порядке in-order (для вывода элементов).
    """
    _inorder(treap.root)

def _inorder(root):
    """
    Вспомогательная функция для обхода in-order.
    """
    if root:
        _inorder(root.left)
        print(f"Key: {root.key}, Priority: {root.priority}")
        _inorder(root.right)

def print_tree(node, prefix="", is_left=True):
    """
    Рекурсивно выводит дерево в консоль.
    :param node: Текущий узел.
    :param prefix: Префикс для отступов.
    :param is_left: Флаг, указывающий, является ли узел левым потомком.
    """
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + f"Key: {node.key}, Priority: {node.priority}")
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

