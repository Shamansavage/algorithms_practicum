# Значение в любой вершине не меньше, чем значения её потомков[
# Глубина всех листьев (расстояние до корня) отличается не более чем на 1 слой.
# heapq алгоритм хранения кучи
# Данный модуль обеспечивает реализацию алгоритма очереди кучи, также известного как алгоритм приоритетной очереди.
# Кучи — это бинарные деревья, для которых каждый родительский узел имеет значение, меньшее или равное любому из его дочерних элементов

import heapq
from collections import Counter
from collections import namedtuple

# класс для хранения в структуре дерева  ( left right - потомки)
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
# обход дерева
        self.left.walk(code, acc + "0")
        self.right.walk(code,acc + "1")

# класс для листьев
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):

        code[self.char] = acc or "0"
# кодирование строки в код Хаффмана ( h = [] - очередь с приоритетами
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():     # очередь с помощью цикла с частотой символа
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)                          # счетчик
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)     # минимальная частота в левый узел
        freq2, _count2, right= heapq.heappop(h)
# внутренний узел потомков
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count +=1
    code = {}   # словарь
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")         # обход дерева от корня
    return code

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

if __name__ == "__main__":
    main()
