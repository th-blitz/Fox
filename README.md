# Fox

## Fox Installation.

1. Install python version 3.8.x in Fox\python\python38 folder without adding to path.
2. Install python version 3.9.x in Fox\python\python39 folder without adding to path.
3. Add Fox\foxy folder to user PATH environment variable.

        setx "PATH=C:\Fox\foxy\;%PATH%"
    
4. Fox Installation is done.

## Open Terminal.

1. Enter `foxy` to initialize fox.
 
        C:\Users\>foxy
        - selected python39
        - foxy py_version
        - foxy exit
   
   You can use python 39 inside (F_39) in any way you wish which is completly isolated from other python 
   installations in the system.

        (PY_39) C:\Users\>python
        Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

2. Enter `foxy 38` to close the current python 39 and initialize python 38.

        (PY_39) C:\Users\>foxy 38
        - selected python38
        - foxy py_version
        - foxy exit
        
   You can use python 38 inside (F_38) in any way possible.

        (PY_38) C:\Users\>python
        Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

3. Enter `foxy exit` to completly exit out of fox.

        (PY_38) C:\Users\>foxy exit

        C:\Users\>
        
        

