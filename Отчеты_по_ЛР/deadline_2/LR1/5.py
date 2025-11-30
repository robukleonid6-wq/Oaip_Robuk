stroka = input("введи строку: ")
answer = ""
i = 0

while i < len(stroka):
    if stroka[i] not in "аеёиоуыэюяaeiouАЕЁИОУЫЭЮЯAEIOU":
        answer = answer + stroka[i]
    i = i + 1

print(answer)