import ast
import os.path

formats = {'black': '\x1b[30m', 'red': '\x1b[31m', 'green': '\x1b[32m',
'yellow': '\x1b[33m', 'blue': '\x1b[34m', 'purple': '\x1b[35m', 'cyan': '\x1b36m'}

def fmat(string, fmat):
    return str(formats[fmat] + string + '\x1b[0m')