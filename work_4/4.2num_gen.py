def prime_generator():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1 if num == 2 else 2  


gen = prime_generator()
for i in range(20):  
    print(next(gen))