# ------------------------------------------------------------------------------
# 
# Description of this module.
# 
# ------------------------------------------------------------------------------
# Example for doctest:
#
# python __init__.py
#
# ------------------------------------------------------------------------------

__copyright__ = "Copyright 2023 - HZE B.V."
__license__   = "G"
__author__    = "Daniël Hendriks"
__contact__   = "daan@hze.nl"
__date__      = "2023-07-24"
__version__   = "V0.0.1"
__status__    = "Development"

__all__ = ["function"]


if __name__ == "__main__":
    from function import *
else:
    from .function import *


def main():
    import doctest
    for count in range(10):
        (failures, tests) = doctest.testmod()
        if failures:
            break
    print("Doctests OK")


if __name__ == "__main__":
    main()

