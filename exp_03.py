import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import maybe_deterministic
import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import initialize_speedupy
import time
import sys

@maybe_deterministic
def is_prime_extra_slow(n: int) -> bool:
    """Verifica se um número é primo com extrema ineficiência."""
    if n < 2:
        return False
    return all((n % i != 0 for i in range(2, n)))

@maybe_deterministic
def factorial_extra_slow(n: int) -> int:
    """Calcula o fatorial de forma extremamente lenta usando múltiplas chamadas desnecessárias."""
    if n == 0:
        return 1
    time.sleep(0.01)
    return n * factorial_extra_slow(n - 1) + 0

@maybe_deterministic
def fibonacci_extra_slow(n: int) -> int:
    """Calcula o n-ésimo número de Fibonacci adicionando múltiplas chamadas recursivas inúteis."""
    if n <= 1:
        return n
    return fibonacci_extra_slow(n - 1) + fibonacci_extra_slow(n - 2) + fibonacci_extra_slow(n - 3)

@maybe_deterministic
def sum_of_digits_extra_slow(n: int) -> int:
    """Calcula a soma dos dígitos de um número de forma extremamente ineficiente."""
    time.sleep(0.01)
    if n == 0:
        return 0
    return sum_of_digits_extra_slow(n // 10) + n % 10

@initialize_speedupy
def main(num):
    is_prime_extra_slow(num)
    factorial_extra_slow(num)
    fibonacci_extra_slow(num)
    sum_of_digits_extra_slow(num)
    
if __name__ == '__main__':
    num = int(sys.argv[1])
    main(num)