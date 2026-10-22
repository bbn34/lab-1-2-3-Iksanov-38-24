from math import fabs

xb = float(input("Xнач = "))
xe = float(input("Xкон = "))
dx = float(input("dx = "))
eps = float(input("epsilon = "))

x = xb

print("+----------+------------+--------+")
print("|    X     |    Si(X)   | Члены  |")
print("+----------+------------+--------+")

while x <= xe + 1e-12:
    term = x
    s = term
    n = 0

    while fabs(term) > eps:
        n += 1
        term *= -x * x * (2 * n - 1) / ((2 * n + 1) ** 2 * (2 * n))
        s += term

    print(f"| {x:8.3f} | {s:10.6f} | {n+1:6d} |")
    x += dx

print("+----------+------------+--------+")
