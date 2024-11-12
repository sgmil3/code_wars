"""
Name: Square into Squares. Protect trees!
Link: https://www.codewars.com/kata/54eb33e5bc1a25440d000891
Level: 4kyu
Desc.: Decompose a number into a sum of squares
Finished: Yes
"""

from functools import lru_cache


def decompose(n):
    @lru_cache(maxsize=None)
    def _decompose(n, i):
        if n == 0:
            return []
        if n < 0:
            return None
        for j in range(i, 0, -1):
            res = _decompose(
                n - j**2, j - 1 if n - j**2 > (j - 1) ** 2 else int((n - j**2) ** 0.5)
            )
            if res is not None:
                return res + [j]
        return None

    return _decompose(
        n**2, n - 1  # if n - (n-1)**2 > (n - 1) ** 2 else int((n - (n-1)**2) ** 0.5)
    )


if __name__ == "__main__":
    print(decompose(50))
    print(decompose(50))
