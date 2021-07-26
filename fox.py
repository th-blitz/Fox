import sys
import os


if __name__ == '__main__':
        
    command = str(sys.argv[1])

    try:
        arg_2 = str(sys.argv[2])
    except:
        arg_2 = None
        pass

    try:
        arg_3 = str(sys.argv[3])
    except:
        arg_3 = None
        pass

    os.system(f'python bridge.py {command} {arg_2} {arg_3}')
