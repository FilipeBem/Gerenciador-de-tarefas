import cx_Freeze

executables = [cx_Freeze.Executable('gerenciador.py')]

cx_Freeze.setup(
    name="Gerenciador de Tarefas",
    options={'build_exe': {'packages':['PySimpleGUI']}},

    executables = executables
    
)