import os
import time
import threading
import keyboard
import pyautogui
from colorama import Fore, Style, init

init(autoreset=True)

logo = f""" {Fore.MAGENTA}
("`-''-/").___..--''"`-._ 
 `6_ 6  )   `-.  (     ).`-.__.`) 
 (_Y_.)'  ._   )  `._ `. ``-..-' 
   _..`--'_..-_/  /--'_.' 
  ((((.-''  ((((.'  (((.-' 
    {Style.RESET_ALL}"""

def print_interface(active, click_type):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(Fore.YELLOW + "------------------------------------------------")
    print(Fore.MAGENTA + " Click Hold - By Sketchi")
    print(Fore.GREEN + " [F5]  -> On/Off the ClickHold (Left Click)")
    print(Fore.GREEN + " [F6]  -> On/Off the ClickHold (Right Click)")
    print(Fore.RED + " [ESC] -> Exit")
    print(Fore.YELLOW + "------------------------------------------------")
    click_status = f"\n [ Statut du clic : {Fore.GREEN}ACTIF 🟢{Style.RESET_ALL} " if active else f"\n [ Statut du clic : {Fore.RED}INACTIF 🔴{Style.RESET_ALL} "
    print(click_status + f"({click_type})")
    print(Fore.BLUE + "\n En attente d'une action...\n")

clicker_active = False
running = True
click_type = 'left'

def clicker_thread():
    while running:
        if clicker_active:
            pyautogui.mouseDown(button=click_type)
            while clicker_active and running:
                time.sleep(0.1)
            pyautogui.mouseUp(button=click_type)
        else:
            time.sleep(0.1)

def toggle_clicker(button):
    global clicker_active, click_type
    if click_type == button:
        clicker_active = not clicker_active
    else:
        click_type = button
        clicker_active = True 
    print_interface(clicker_active, click_type)

def stop_script():
    global running
    running = False
    print(Fore.RED + "\nArrêt du script...")
    os._exit(0)

print_interface(clicker_active, click_type)

threading.Thread(target=clicker_thread, daemon=True).start()

keyboard.add_hotkey("f5", lambda: toggle_clicker('left'))
keyboard.add_hotkey("f6", lambda: toggle_clicker('right'))
keyboard.add_hotkey("esc", stop_script)

keyboard.wait()
