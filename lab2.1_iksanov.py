from math import sqrt

x = float(input("Введите x: "))

if x < 0:
    y = -0.5 * x - 3
elif 0 <= x < 3:
    y = -sqrt(2.25 - (x - 1.5) ** 2)
elif 3 <= x < 6:
    y = sqrt(9 - (x - 6) ** 2)
else:
    y = 3

print(f"X = {x:.2f}; Y = {y:.2f}")
