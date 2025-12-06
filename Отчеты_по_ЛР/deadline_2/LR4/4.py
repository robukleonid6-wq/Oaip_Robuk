temperatury = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]

print("Температуры за 14 дней:")
print(temperatury)

samaia_vysokaia = temperatury[0]  
for temp in temperatury:
    if temp > samaia_vysokaia:
        samaia_vysokaia = temp
print("Самая высокая температура: " + str(samaia_vysokaia) + "°C")

samaia_nizkaia = temperatury[0]
for temp in temperatury:
    if temp < samaia_nizkaia:
        samaia_nizkaia = temp
print("Самая низкая температура: " + str(samaia_nizkaia) + "°C")

summa_temp = 0
for temp in temperatury:
    summa_temp = summa_temp + temp

sredniaia_temp = summa_temp / len(temperatury)
print("Средняя температура: " + str(sredniaia_temp) + "°C")

dney_vyshe_srednei = 0
for temp in temperatury:
    if temp > sredniaia_temp:
        dney_vyshe_srednei = dney_vyshe_srednei + 1
print("Дней с температурой выше средней: " + str(dney_vyshe_srednei))

otsortirovannye_temp = temperatury.copy()

dlina_spiska = len(otsortirovannye_temp)
for i in range(dlina_spiska):
    for j in range(0, dlina_spiska - i - 1):
        if otsortirovannye_temp[j] > otsortirovannye_temp[j + 1]:
            
            temp_var = otsortirovannye_temp[j]
            otsortirovannye_temp[j] = otsortirovannye_temp[j + 1]
            otsortirovannye_temp[j + 1] = temp_var

print("Отсортированные температуры по возрастанию:")
print(otsortirovannye_temp)

temperatury_farengeit = []
for temp in temperatury:
    temp_f = temp * 9/5 + 32
    temperatury_farengeit.append(temp_f)

print("Температуры в Фаренгейтах:")
print(temperatury_farengeit)

print("\nСводка по температурам:")
print("Температуры в Цельсиях: ", temperatury)
print("Максимальная: ", samaia_vysokaia, "°C")
print("Минимальная: ", samaia_nizkaia, "°C")
print("Средняя: ", sredniaia_temp, "°C")
print("Дней выше средней: ", dney_vyshe_srednei)
print("Отсортированный список: ", otsortirovannye_temp)
print("Температуры в Фаренгейтах: ", temperatury_farengeit)