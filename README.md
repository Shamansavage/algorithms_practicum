# 2.1 Кодирование строки по алгоритму Хаффмана
По данной строчке, состоящей из строчных букв латинского алфавита:

Errare humanum est.

постройте оптимальный беспрефиксный код на основании классического алгоритма кодирования Хаффмана.

В результате выполнения, функция huffman_encode() должна вывести на экран в первой строке — количество уникальных букв, встречающихся в строке и размер получившейся закодированной строки в битах. В следующих строках запишите коды символов в формате "'symbol': code". В последней строке выведите саму закодированную строку.

Пример вывода для данного текста:

12 67
' ': 000
'.': 1011
'E': 0110
'a': 1110
'e': 1111
'h': 0111
'm': 010
'n': 1000
'r': 110
's': 1001
't': 1010
'u': 001
0110110110111011011110000111001010111010000010100001111100110101011

