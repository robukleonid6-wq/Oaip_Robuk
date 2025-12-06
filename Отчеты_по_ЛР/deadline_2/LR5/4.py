vvodimiy_tekst = input("введите текст: ")

znaki = [",", ".", "!", "?", ";", ":", "-", "—", "(", ")", "[", "]", "{", "}", "\"", "'"]
chistiy_tekst = vvodimiy_tekst
for znak in znaki:
    chistiy_tekst = chistiy_tekst.replace(znak, " ")

slova = chistiy_tekst.split()
slova_nizhniy_registr = []
for slovo in slova:
    slova_nizhniy_registr.append(slovo.lower())

unikalnie_slova = set(slova_nizhniy_registr)

print(f"уникальные слова: {len(unikalnie_slova)}")

dlinnie_slova = set()
for slovo in unikalnie_slova:
    if len(slovo) > 5:
        dlinnie_slova.add(slovo)

print(f"длинные слова: {dlinnie_slova}")

klyuchevoe_slovo1 = "okynsev"
klyuchevoe_slovo2 = "vodolaz"

naydeno_klyuchevoe = False
if klyuchevoe_slovo1 in unikalnie_slova or klyuchevoe_slovo2 in unikalnie_slova:
    naydeno_klyuchevoe = True

print(f"найдены ключевые слова: {naydeno_klyuchevoe}")