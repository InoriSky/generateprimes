ITERATIONS_PER_EXECUTION = 100000
TICK_SIZE_SMALL = 2000
TICK_SIZE_BIG = 10000

def isprime(x, s):
    for i in list(s):
        if x % i == 0:
            return False
    return True

try:
    f = open('primes.txt', 'r')
    start = ''
    while (1):
        c = f.read(1)
        if c.isnumeric():
            start += c
        else:
            break
    start = int(start)
    primes = eval(f.read())
    f.close()
except FileNotFoundError:
    start = 1
    primes = {2}

i = start
while i - start <= ITERATIONS_PER_EXECUTION:
    if isprime(2*i+1, primes):
        primes.add(2*i+1)
    i += 1

    if i % TICK_SIZE_SMALL == 0:
        print('.')
    if i % TICK_SIZE_BIG == 0: 
        print('{} numbers tested'.format(i))
        
f = open('primes.txt', 'w')
f.write(str(i))
f.write(' ')
f.write(str(primes))

print('Tested up to {}'.format(str(2*i+1)))
f.close()