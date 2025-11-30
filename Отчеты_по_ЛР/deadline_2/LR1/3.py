text = input("введите строку: ")
good_text = text.lower().replace(" ", "")

left = 0
right = len(good_text) - 1
is_palindrome = True

while left < right:
    if good_text[left] != good_text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("да, это палиндром")
else:
    print("это не палиндром")