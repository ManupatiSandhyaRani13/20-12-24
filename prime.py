def is_prime(n):
    is_prime = True
    if n == 1:
        is_prime = False
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not prime number")


n = int(input("Enter a number : "))
is_prime(n)
