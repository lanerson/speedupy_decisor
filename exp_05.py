import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import maybe_deterministic
import sys
sys.path.append('/home/lanerson/Documentos/multiprocess_exps')
from speedupy.speedupy import initialize_speedupy
import sys

@maybe_deterministic
def soma_rapida(n):
    return n * (n + 1) // 2

@maybe_deterministic
def multiplicacao_rapida(n):
    return n * (n - 1)

@maybe_deterministic
def soma_lenta(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

@maybe_deterministic
def multiplicacao_lenta(n):
    total = 0
    for i in range(1, n):
        total += n - 1
    return total

@initialize_speedupy
def main(n):
    soma_rapida(n)
    multiplicacao_rapida(n)
    soma_lenta(n)
    multiplicacao_lenta(n)
if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)