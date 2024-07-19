# main.py

def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("O número n deve ser maior que zero")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev2 = 0  # Fib(1)
        fib_prev1 = 1  # Fib(2)
        fib_current = 0

        for _ in range(3, n + 1):
            fib_current = fib_prev1 + fib_prev2
            fib_prev2 = fib_prev1
            fib_prev1 = fib_current

        return fib_current

# Exemplos de uso:
if __name__ == "__main__":
    # Testando a função com alguns valores
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
