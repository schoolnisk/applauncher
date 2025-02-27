
from rich.console import Console
import subprocess
import time



menu = """\n
    Settings -------  1\n
    Ip a -----------  2\n
    Clock ----------  3\n
    Quit -----------  0\n      
"""

setting = """\n
    Add cmd/fld ----- 1\n
    Rm cmd/fld ------ 2\n
    Back ------------ 0\n
"""

bol = True

console = Console()

def run(cmd):
    return subprocess.run(cmd)

def clear():
    return subprocess.run(["clear"])

def add():
    return console.print("not working", style="bold red") 

def rm():
    return console.print("not working", style="bold red") 


clear()

while bol == True:
    
    console.print(menu, style="bold green")
    
    try:
        console.print("    enter selection\n", style="bold blue")
        ask = int(input("    "))
    
    except ValueError:
        clear()
        console.print(" no", "numbers", style="bold red")
        time.sleep(1)
        clear()
    
    clear()
    
    if ask == 0:
        bol = False
    
    elif ask == 1:
        console.print(setting, style="bold green")
        console.print("\n    enter your selection", style="bold blue")
        ask = int(input("    "))

        if ask == 0:
            clear()

        elif ask == 1:
            clear()
            add()

        elif ask == 2:
            clear()
            rm()
    
    elif ask == 2:
        run(["ip", "a"])
        console.print("[bold blue]Quit?[/bold blue] [bold red](y/n)[/bold red]")
        ask = input("   ")
        clear()
        
        if ask == "y":
            bol = False

    elif ask == 3:
        run(["tty-clock"])
        console.print("[bold blue]Quit?[/bold blue] [bold red](y/n)[/bold red]")
        ask = input("   ")
        clear()
        
        if ask == "y":
            bol = False
        

    
            
        

