R = float(input("Введите R: "))
x = float(input("Введите x: "))
y = float(input("Введите y: "))

circle = (x * x + y * y <= R * R) and (y >= 0)
triangle = (-R <= x <= 0) and (-R <= y <= x)

if circle or triangle:
    print("Попадает")
else:
    print("Не попадает")
