from math import sqrt

def is_prime(n: int) -> bool:

    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Revisamos si el numero esta compuesto por
    # un numero primo diferente de 2 y 3.
    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def main():
    if is_prime(4):
        print("El numero es primo")
    else:
        print("El numero NO es primo")


if __name__ == '__main__':
    main()