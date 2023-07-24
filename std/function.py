# ------------------------------------------------------------------------------
# 
# Description of this module.
# 
# ------------------------------------------------------------------------------
# Example for doctest:
#
# python functions.py
#
# ------------------------------------------------------------------------------

__copyright__ = "Copyright 2023 - HZE B.V."
__license__   = ""
__author__    = "Daniël Hendriks"
__contact__   = "daan@hze.nl"
__date__      = "2023-07-24"
__version__   = "V0.0.1"
__status__    = "Development"

__all__ = ["Test"]

class Test:

    # Returns the greatest common divisor of p and q
    @staticmethod
    def testing(p: int, q: int) -> int:
        """
        >>> Test.testing(48, 180)
        12
        """
        while q != 0:
            (p, q) = (q, p % q)
        return p


def main():
    import doctest
    for count in range(10):
        (failures, tests) = doctest.testmod()
        if failures:
            break
    print("Doctests OK")


if __name__ == "__main__":
    main()

