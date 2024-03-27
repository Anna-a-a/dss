import heapq

# Исходный текст
text = ("БЫТЬ ЭНТУЗИАСТКОЙ СДЕЛАЛОСЬ ЕЕ ОБЩЕСТВЕННЫМ ПОЛОЖЕНИЕМ И ИНОГДА КОГДА ЕЙ ДАЖЕ ТОГО НЕ ХОТЕЛОСЬ ОНА ЧТОБЫ "
       "НЕ ОБМАНУТЬ ОЖИДАНИЙ ЛЮДЕЙ ЗНАВШИХ ЕЕ ДЕЛАЛАСЬ ЭНТУЗИАСТКОЙ СДЕРЖАННАЯ УЛЫБКА ИГРАВШАЯ ПОСТОЯННО НА ЛИЦЕ "
       "АННЫ ПАВЛОВНЫ ХОТЯ И НЕ ШЛА К ЕЕ ОТЖИВШИМ ЧЕРТАМ ВЫРАЖАЛА КАК У ИЗБАЛОВАННЫХ ДЕТЕЙ ПОСТОЯННОЕ СОЗНАНИЕ СВОЕГО "
       "МИЛОГО НЕДОСТАТКА ОТ КОТОРОГО ОНА НЕ ХОЧЕТ НЕ МОЖЕТ И НЕ НАХОДИТ НУЖНЫМ ИСПРАВЛЯТЬСЯ В  СЕРЕДИНЕ РАЗГОВОРА "
       "ПРО ПОЛИТИЧЕСКИЕ   ДЕЙСТВИЯ АННА ПАВЛОВНА РАЗГОРЯЧИЛАСЬ АХ НЕ ГОВОРИТЕ МНЕ ПРО АВСТРИЮ Я НИЧЕГО НЕ ПОНИМАЮ "
       "МОЖЕТ БЫТЬ НО АВСТРИЯ НИКОГДА НЕ ХОТЕЛА И НЕ ХОЧЕТ ВОЙНЫ ОНА ПРЕДАЕТ  НАС РОССИЯ ОДНА ДОЛЖНА БЫТЬ "
       "СПАСИТЕЛЬНИЦЕЙ ЕВРОПЫ")

# Подсчет встречаемости символов
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1


# Построение префиксного кода Хаффмана
def build_huffman_tree(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def build_huffman_code(tree):
    huffman_code = {}
    for symbol, code in tree:
        huffman_code[symbol] = code
    return huffman_code


tree = build_huffman_tree(frequency)
huffman_code = build_huffman_code(tree)

# Вычисление избыточности кода
total_length = 0
for symbol, code in huffman_code.items():
    total_length += len(code) * frequency[symbol]

total_symbols_count = sum(frequency.values())
redundancy = total_length / total_symbols_count

# Вывод результатов
print("Префиксный код Хаффмана:", huffman_code)
print("Избыточность кода:", redundancy)
print("Частотность символов:")
text_length = len(text)
for char, freq in frequency.items():
    print(f"{char}: {freq / text_length}")
