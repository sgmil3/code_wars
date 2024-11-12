"""
Name: Prime Streaming (PG-13)
Link: https://www.codewars.com/kata/5519a584a73e70fa570005f5
Level: 3kyu
Desc.: Generate a stream of prime numbers
Finished: Yes
"""

import itertools


class Primes:
    @staticmethod
    def stream():
        D = {9: 3, 25: 5}
        yield 2
        yield 3
        yield 5
        MASK = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
        MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

        for q in itertools.compress(
            itertools.islice(itertools.count(7), 0, None, 2), itertools.cycle(MASK)
        ):
            p = D.pop(q, None)
            if p is None:
                D[q * q] = q
                yield q
            else:
                x = q + 2 * p
                while x in D or (x % 30) not in MODULOS:
                    x += 2 * p
                D[x] = p


def verify(from_n, *vals):
    stream = Primes.stream()
    for _ in range(from_n):
        next(stream)
    for v in vals:
        assert next(stream) == v
        print("Verified: ", v)


if __name__ == "__main__":
    verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    verify(100, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601)
    verify(1000, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017)
