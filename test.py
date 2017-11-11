import cProfile
import test2

a = 'None'

def test_func(p1, p2):
    var = 0
    for e in range(10):
        var += e
        p1 *= var
        p2 /= var**e
    
    return p1 + p2

def f(x):
    return x**2-x

def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

def primes(kmax):
    p = [None] * 1000
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

class Halley():
    def archer(self):
        return 1

def main():
    print f(1)
    print primes(45)
    test_func(3, 4)

    h = Halley()
    print h.archer()

if __name__ == "__main__":
    main()

#cProfile.run('integrate_f(10, 20, 10000)')
#cProfile.run('test2.integrate_f2(10, 20, 10000)')

#cProfile.run('primes(10000)')
#cProfile.run('test2.primes(10000)')