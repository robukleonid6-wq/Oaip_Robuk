print("введите текст (для завершения введи пустую строку):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

full_text = " ".join(lines)

import string
translator = str.maketrans('', '', string.punctuation)
clean_text = full_text.translate(translator).lower()

words = clean_text.split()
word_stats = {}

for word in words:
    if word in word_stats:
        word_stats[word] += 1
    else:
        word_stats[word] = 1

print("Статистика слов:", word_stats)