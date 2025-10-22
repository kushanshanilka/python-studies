import sys
import math
import cmath

#!/usr/bin/env python3
"""
Compute roots of a quadratic equation ax^2 + bx + c = 0.

Usage:
- Run interactively and enter a, b, c when prompted, or
- Provide a b c on the command line: python kushan.py 1 -3 2
"""

def quadratic_roots(a: float, b: float, c: float):
    if a == 0.0:
        # Linear or degenerate
        if b == 0.0:
            return ("no_solution" if c != 0.0 else "infinite_solutions",)
        return (-c / b,)
    disc = b * b - 4 * a * c
    if disc >= 0:
        sqrt_d = math.sqrt(disc)
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
    else:
        sqrt_d = cmath.sqrt(disc)
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
    return (r1, r2)

def parse_args(argv):
    if len(argv) == 4:
        try:
            return float(argv[1]), float(argv[2]), float(argv[3])
        except ValueError:
            pass
    # fallback to interactive input
    while True:
        try:
            parts = input("Enter coefficients a b c separated by spaces: ").strip().split()
            a, b, c = map(float, parts)
            return a, b, c
        except Exception:
            print("Invalid input. Please enter three numbers (e.g. 1 -3 2).")

if __name__ == "__main__":
    a, b, c = parse_args(sys.argv)
    roots = quadratic_roots(a, b, c)
    if roots == ("no_solution",):
        print("No solution (0x + 0 = nonzero).")
    elif roots == ("infinite_solutions",):
        print("Infinite solutions (0x + 0 = 0).")
    elif len(roots) == 1:
        print(f"Linear root: {roots[0]}")
    else:
        r1, r2 = roots
        if isinstance(r1, complex) or isinstance(r2, complex):
            print(f"Complex roots: {r1} , {r2}")
        else:
            if math.isclose(r1, r2):
                print(f"One real repeated root: {r1}")
            else:
                print(f"Real roots: {r1} , {r2}")