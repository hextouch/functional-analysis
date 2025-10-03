"""
Banach fixed-point theorem: contraction mapping
"""
def contraction(x):
    return 0.5 * x

x0 = 10.0
for i in range(10):
    x0 = contraction(x0)
    print(f"Iteration {i+1}: {x0}")
