def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    result = []
    for num in range(start, end+1):
        if is_prime(num):
            result.append(num)
    return result

start = int(input("Enter start: "))
end = int(input("Enter end: "))
primes = primes_in_range(start, end)
print("Prime numbers:", primes)
