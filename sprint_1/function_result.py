def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return a * x ** 2 + b * x + c


a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
