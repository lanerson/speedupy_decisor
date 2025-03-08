import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import maybe_deterministic
import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import initialize_speedupy
import math
import sys

@maybe_deterministic
def is_prime(n: int) -> bool:
    """Verifica se um número é primo de forma otimizada."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@maybe_deterministic
def factorial(n: int) -> int:
    """Calcula o fatorial de um número de forma otimizada."""
    return math.factorial(n)

@maybe_deterministic
def fibonacci(n: int) -> int:
    """Retorna o n-ésimo número de Fibonacci usando a fórmula fechada (Binet)."""
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))

@maybe_deterministic
def sum_of_digits(n: int) -> int:
    """Calcula a soma dos dígitos de um número de forma eficiente."""
    return sum(map(int, str(n)))

@initialize_speedupy
def main(num):
    is_prime(num)
    factorial(num)
    fibonacci(num)
    sum_of_digits(num)
if __name__ == '__main__':
    num = int(sys.argv[1])
    main(num)