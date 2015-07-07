__author__ = 'myatsko'
def create_primes(max_n):
    """ creating primes up to a maximum value using a sieve algorithm. All
        multiples of a prime are flagged as 'no prime'. In addition there
        is an optimization by ignoring values flagged as none prime when
        proceeding to next value."""
    sieve  = [False, True] * (max_n // 2)
    sieve += [False]

    sieve[1] = False
    sieve[2] = True
    primes   = [2]

    val = 3
    while val <= max_n:
        # now we have one prime
        primes.append(val)
        # strike out values not being a prime
        offset  = val * 2
        noprime = val + offset
        while noprime <= max_n:
            sieve[noprime] = False
            noprime += offset
        # next value
        val += 2
        while val <= max_n:
            if not sieve[val]:
                val += 2
            else:
                break

    return primes

summ = 0

for z in create_primes(2000000):
    summ += z
    print z, summ
