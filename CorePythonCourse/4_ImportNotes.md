notes:

from REPL:

# import testImport -> for the complete file execution (only blocks outside if __name__ == "__main__")

# from testImpport import $funcion$ -> for a specific function, and then use it

# from testImport import * -> to import the complete file

# to RELOAD the file imported -> import importlib -> then in the repl do: importlib.reload(MODULE_NAME) -> then if you are using a function from that module, do again "from MODULE_NAME import FUNCTION_NAME"

## DOCSTRING ##

"""for document purpose. THEY MUST be the first statement int he blocks for constructs. args and return are specified"""


## MAKE SCRIPT EXECUTABLE ##

# shebang -> #! usr/bin/env python3  #this is to specifiy the py interpreter i gonna use 

# executable -> chmod +x weatherAPI.py (se corre con ./weatherAPI.py)BEFORE THE SHEBANG . no se si el chmod es en la terminal o en el modulo de python

