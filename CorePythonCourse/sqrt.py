import sys

def sqrt(x):

    """compute square roots using method of heron of alexandia

    Args:
        the number to be sqrted

    Returns: sqrt(x)

    Raises:
        ValueError: If x is nengative 
        
    """
 
    if x < 0:
        raise ValueError(
            "Cannot compute square root of " 
            f"negative number {x}"
        )


    guess = x
    i = 0

    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("THIS IS NEVER PRINTED!")
    except ValueError as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()