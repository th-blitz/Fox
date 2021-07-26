import sys
import os

def exe_python():

    path , _ = os.path.split(sys.executable)
    print(path)

def ver():

    ver = str(sys.version).split(' ')[0]

    print(ver)


if __name__ == "__main__":

    try:
        arg_1 = str(sys.argv[1])
    except:
        arg_1 = None
        pass

    try:
        arg_2 = str(sys.argv[2])
    except:
        arg_2 = None
        pass

    if arg_1 == 'exe_python':
        exe_python()

    elif arg_1 == 'ver':
        ver()
