from commonfunctions import isPrime

def problem27():
    MAX_RANGE = 1_000

    maximum_consecutives = 0
    maximum_coeficients = (None, None)
    
    for a in range(-MAX_RANGE+1, MAX_RANGE,2):
        for b in range(-MAX_RANGE+1, MAX_RANGE+1,2):
    
            formula = lambda n: (n*n)+(a*n)+b
            n=0
            current_result = formula(n)
            
            while isPrime(current_result):
                n=n+1
                current_result = formula(n) 
            
            if maximum_consecutives<n:
                maximum_consecutives = n
                maximum_coeficients = (a, b)
    print(f"The product of the coefficients, a and b, for the quadratic expression that produces the maximum ({maximum_consecutives}) number of primes for consecutive values (x²+({maximum_coeficients[0]})+({maximum_coeficients[1]}x) is {maximum_coeficients[0] * maximum_coeficients[1]}")
