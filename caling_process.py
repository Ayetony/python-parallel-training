import os
import sys


program = 'python'
print('process calling')
arguments = ['called_process.py']

os.execvp(program, (program,) + tuple(arguments))
print('good bye')


