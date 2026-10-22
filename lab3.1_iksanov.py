from math import sqrt

xb = float(input("X нач = "))
xe = float(input("X кон = "))
dx = float(input("dx = "))

x = xb
print("+----------+----------+")
print("|    X     |    Y     |")
print("+----------+----------+")

while x <= xe + 1e-9:
    if x < 0:
        y = -0.5 * x - 3
    elif x < 3:
        y = -sqrt(2.25 - (x - 1.5) ** 2)
    elif x < 6:
        y = sqrt(9 - (x - 6) ** 2)
    else:
        y = 3

    print(f"| {x:8.2f} | {y:8.2f} |")
    x += dx

print("+----------+----------+")
