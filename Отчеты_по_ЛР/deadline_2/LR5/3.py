cveta = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128)
}

cvet1 = "красный"
cvet2 = "синий"

rgb1 = cveta[cvet1]
rgb2 = cveta[cvet2]

smeshamniy_r = (rgb1[0] + rgb2[0]) // 2
smeshamniy_g = (rgb1[1] + rgb2[1]) // 2
smeshamniy_b = (rgb1[2] + rgb2[2]) // 2

smeshamniy_cvet = (smeshamniy_r, smeshamniy_g, smeshamniy_b)
print(f"смешиваем {cvet1} {rgb1} и {cvet2} {rgb2}")
print(f"получился цвет: {smeshamniy_cvet}")

cvet_dlya_inversii = "красный"
rgb_inversiya = cveta[cvet_dlya_inversii]

inversiya_r = 255 - rgb_inversiya[0]
inversiya_g = 255 - rgb_inversiya[1]
inversiya_b = 255 - rgb_inversiya[2]

inversniy_cvet = (inversiya_r, inversiya_g, inversiya_b)
print(f"инвертируем цвет {cvet_dlya_inversii} {rgb_inversiya}")
print(f"инвертированный цвет: {inversniy_cvet}")