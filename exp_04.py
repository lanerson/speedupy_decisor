import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import maybe_deterministic
import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import initialize_speedupy
import time

@maybe_deterministic
def is_prime_ultra_slow(n: int) -> bool:
    """Verifica se um número é primo de forma extremamente ineficiente, verificando divisibilidade múltiplas vezes."""
    if n < 2:
        return False
    for i in range(2, n):
        for _ in range(10):  # Loop redundante para tornar ainda mais lento
            if n % i == 0:
                return False
        time.sleep(0.01)  # Atraso artificial
    return True

@maybe_deterministic
def factorial_ultra_slow(n: int) -> int:
    """Calcula o fatorial de maneira absurdamente ineficiente usando uma pilha simulada."""
    stack = list(range(1, n + 1))
    result = 1
    while stack:
        time.sleep(0.01)  # Atraso artificial
        result *= stack.pop()
    return result

@maybe_deterministic
def collatz_ultra_slow(n: int) -> int:
    """Calcula o número de passos para chegar a 1 na sequência de Collatz, mas com atrasos e redundâncias."""
    steps = 0
    while n != 1:
        time.sleep(0.01)  # Atraso artificial
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

@maybe_deterministic
def reverse_number_ultra_slow(n: int) -> int:
    """Inverte um número inteiro de forma extremamente ineficiente."""
    time.sleep(0.01)  # Atraso artificial
    reversed_num = int(''.join(reversed(str(n))))  # Usa conversões desnecessárias
    return reversed_num

@initialize_speedupy
def main(num):    
    is_prime_ultra_slow(num)
    factorial_ultra_slow(num)
    collatz_ultra_slow(num)
    reverse_number_ultra_slow(num)

if __name__ == "__main__":
    num = int(sys.argv[1])

    main(num)
