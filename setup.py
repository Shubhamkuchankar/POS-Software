import cx_Freeze 
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\The_Shubhamkuchankar\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\The_Shubhamkuchankar\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="Icon.ico")]


cx_Freeze.setup(
    name = "Ganesh Nutrition POS",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["Icon.ico",'tcl86t.dll','tk86t.dll', 'images','fonts','Database','Database/store.db','Database/raw_inventory.csv', 'admin.py','employee.py',]}},
    version = "1.0",
    description = "Ganesh Nutrition POS System | Developed By TSK",
    executables = executables
    )
