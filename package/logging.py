# ------------------------------------------------------------------------------
# 
# Description of this module.
# 
# ------------------------------------------------------------------------------
# Example for doctest:
#
# python logging.py
#
# ------------------------------------------------------------------------------

__copyright__ = "Copyright 2023 - HZE B.V."
__license__   = ""
__author__    = "Daniël Hendriks"
__contact__   = "daan@hze.nl"
__date__      = "2023-07-24"
__version__   = "V0.0.1"
__status__    = "Development"

__all__ = ["Log"]


from datetime import datetime


# Log functions
class Log:

    @staticmethod
    # Get text of date and time
    def get_time() -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    # Write text to file
    @staticmethod
    def text_to_file(filename: str, text: str) -> bool:
        """
        >>> Log.text_to_file("standard.log", "Error")
        True
        """
        try:
            with open(filename, 'a') as file:
                file.write(text + "\n")
            return True
        except:
            return False


    @staticmethod
    # Write text to screen and/or file
    def text_message(filename: str, text: str, screen: bool, file: bool) -> bool:
        """
        >>> Log.text_message("standard.log", "Error", 0, 1)
        True
        """
        if screen:
            print(f"{Log.get_time()} - {text}")
        if file:
            Log.text_to_file(f"{filename}",f"{Log.get_time()} - {text}")
        return True


def main():
    import doctest
    for count in range(10):
        (failures, tests) = doctest.testmod()
        if failures:
            break
    print("Doctests OK")


if __name__ == "__main__":
    main()

