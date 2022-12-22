from commonfunctions import generate_primes, all_perms

def generate_pandigitals(qnt):
    """"This function yields the pandigital numbers based on the length given in the parameter [qnt]."""
    primes = generate_primes(qnt-2)
    for num in all_perms(list(range(qnt+1))):
        num = ''.join(map(str, num))
        result = True
        for i in range(1,len(num)-2):
            subdivision = int(''.join(map(str, [num[i], num[i+1], num[i+2]] )))
            if not subdivision % primes[i-1] == 0:
                result = False
                break
        if result:
            yield int(num)

def problem43(num=9):
    print(sum(generate_pandigitals(num)))

problem43()