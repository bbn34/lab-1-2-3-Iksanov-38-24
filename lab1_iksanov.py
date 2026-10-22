from math import sin, cos, tan

alpha = float(input("Введите alpha (в радианах): "))

z1 = (2 * cos(alpha) * sin(2 * alpha) - sin(alpha)) / (
    cos(alpha) - 2 * sin(alpha) * sin(2 * alpha)
)
z2 = tan(3 * alpha)

print(f"z1 = {z1:.6f}")
print(f"z2 = {z2:.6f}")
