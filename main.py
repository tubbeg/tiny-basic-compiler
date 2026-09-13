
import sys
from compiler import Compiler

# reference: https://en.wikipedia.org/wiki/Tiny_BASIC

def raise_invalid_path(): 
    raise Exception("INVALID SOURCE CODE PATH" + str(sys.argv))



if __name__ == "__main__":
    if len(sys.argv) > 1:
        Compiler().parse(sys.argv[1])
    else:
        raise_invalid_path()