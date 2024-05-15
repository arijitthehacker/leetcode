def isPrime(num: int):
    if num <= 1:
        return False  # If the number is less than or equal to one, it can never be prime.

    for i in range(2, num):
        if num % i == 0:
            return False  # If the number can be divided evenly by any other numbers, it's not prime.

    return True  # Otherwise, it's prime.

if __name__ == '__main__':
    print(isPrime(10))
    print(isPrime(11))
    print(isPrime(2))
