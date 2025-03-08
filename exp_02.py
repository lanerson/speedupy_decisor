import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import maybe_deterministic
import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import initialize_speedupy
import sys

@maybe_deterministic
def is_prime_slow(n: int) -> bool:
    """Verifica se um número é primo de forma ineficiente."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@maybe_deterministic
def factorial_slow(n: int) -> int:
    """Calcula o fatorial de um número de forma recursiva ineficiente."""
    if n == 0:
        return 1
    return n * factorial_slow(n - 1)

@maybe_deterministic
def fibonacci_slow(n: int) -> int:
    """Calcula o n-ésimo número de Fibonacci usando recursão ingênua."""
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

@maybe_deterministic
def sum_of_digits_slow(n: int) -> int:
    """Calcula a soma dos dígitos de um número usando divisão e módulo."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

@initialize_speedupy
def main(num):
    is_prime_slow(num)
    factorial_slow(num)
    fibonacci_slow(num)
    sum_of_digits_slow(num)
if __name__ == '__main__':
    num = int(sys.argv[1])
    main(num)