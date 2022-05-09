"""this is the module docstring where you describe the module usage and purpose"""


import sys


def main():
    """this is the main docstring where you describe the function purpose
    Args:
        valor: valor ficticio para simular arg

    Returns:
        A list of blablabla. When i use help($FILE$) this bring me the whole docstring
    """
    n= sys.argv[0] # argv[0] is the module filename
    print("hello world, your arg is " + n )

if __name__ == "__main__":
    main()

