from rich.console import Console
import subprocess
import time

MENU_FILE = "menu.txt"

console = Console()

def run(cmd):
    subprocess.run(cmd, shell=True)

def clear():
    subprocess.run(["clear"])

def load_menu():
    """Load menu from file into a dictionary."""
    menu = {}
    try:
        with open(MENU_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(" ------ ")
                if len(parts) == 2:
                    cmd, num = parts
                    menu[num] = cmd
    except FileNotFoundError:
        # Default commands
        menu = {
            "1": "settings",
            "2": "ip a",
            "3": "tty-clock",
            "0": "quit"
        }
    return menu

def save_menu(menu):
    """Save menu dictionary to file."""
    with open(MENU_FILE, 'w') as f:
        for num, cmd in menu.items():
            f.write(f"{cmd} ------ {num}\n")

def add():
    console.print("\n    What cmd do you want to add?", style="bold blue")
    cmd = input("    ")
    console.print("\n    What number do you want to assign?", style="bold blue")
    num = input("    ")
    
    menu = load_menu()
    
    if num in menu:
        console.print("ERROR: That number is already assigned", style="bold red")
        time.sleep(1)
        return
    
    menu[num] = cmd
    save_menu(menu)
    console.print("cmd added", style="bold red")
    time.sleep(1)
    

def remove():
    menu = load_menu()
    console.print("\n".join([f"    {cmd} ------ {num}\n" for num, cmd in menu.items()]), style="bold green")
    console.print("\n   Enter the number of the command to remove:", style="bold red")
    num = input("   ")
    
    if num in menu:
        del menu[num]
        save_menu(menu)
        console.print("Command removed!", style="bold red")
        time.sleep(1)
        
    else:
        console.print("ERROR: Command not found!", style="bold red")
        time.sleep(1)
        

def settings():
    setting_menu = """\n
    Add cmd --------- 1\n
    Remove cmd ------ 2\n
    Back ------------ 0\n
"""
    console.print(setting_menu, style="bold green")
    console.print("\n    Enter your selection", style="bold blue")
    choice = input("    ")

    if choice == "1":
        clear()
        add()
    elif choice == "2":
        clear()
        remove()


# Main Loop
while True:
    clear()
    menu = load_menu()
    
    console.print("\n".join([f"\n    {cmd} ------ {num}" for num, cmd in menu.items()]), style="bold green")
    
    console.print("\n    Enter selection:", style="bold blue")
    choice = input("    ").strip()
    
    clear()
    
    if choice == "0":
        break
    elif choice == "1":
        settings()
    elif choice in menu:
        run(menu[choice])
        console.print("[bold blue]Quit?[/bold blue] [bold red](y/n)[/bold red]")
        if input("   ").strip().lower() == "y":
            break
    else:
        console.print("Invalid choice! Try again.", style="bold red")
        time.sleep(1)
        clear()
