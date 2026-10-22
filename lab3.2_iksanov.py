from random import uniform

R = float(input("Введите R: "))

print("       X        Y      Результат")
print("--------------------------------")

for i in range(10):
    x = uniform(-R, R)
    y = uniform(-R, R)

    circle = (x * x + y * y <= R * R) and (y >= 0)
    triangle = (-R <= x <= 0) and (-R <= y <= x)

    if circle or triangle:
        result = "Попадает"
    else:
        result = "Не попадает"

    print(f"{x:8.3f} {y:8.3f}   {result}")