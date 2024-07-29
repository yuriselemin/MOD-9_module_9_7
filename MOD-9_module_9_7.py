

# Домашнее задание по теме "Декораторы"
def is_primes(func):
    def wrapper(*args):
        result_ = func(*args)
        if result_ > 1:
            for i in range(2, int(result_ ** 0.5) + 1):
                if result_ % i == 0:
                    return 'Составное'
        return 'Простое'
    return wrapper


@is_primes
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c


result = sum_three(2, 3, 6)
print(result)