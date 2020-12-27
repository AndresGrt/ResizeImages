from cx_Freeze import setup, Executable

setup( name = "ventana",
        version = "0.1",
       executables = [Executable("ResizeAndCut.py")],)
