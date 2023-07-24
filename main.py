# ------------------------------------------------------------------------------
# 
# Description of this module.
# 
# ------------------------------------------------------------------------------
# Example:
#
# python main.py
#
# ------------------------------------------------------------------------------

__copyright__ = "Copyright 2023 - HZE B.V."
__license__   = ""
__author__    = "Daniël Hendriks"
__contact__   = "daan@hze.nl"
__date__      = "2023-07-24"
__version__   = "V0.0.1"
__status__    = "Development"


import package


def main():
    print(package.Test.testing(48, 180))
    package.Log.text_message("standard.log", "Error", 1, 1)


if __name__ == "__main__":
    main()

