import tkinter as tk
import psutil
import time
import sys

root = tk.Tk()
root.title("ProTask - Wiktor Nosarzewski")
root.geometry("280x90")
root.attributes('-topmost', True)
root.attributes('-alpha', 0.5) # Dodanie przezroczystości
root.overrideredirect(True) # Usunięcie dekoracji okna
root.geometry("+0+0") # Ustawienie pozycji okna na lewy górny róg ekranu

text = tk.Text(root, bg="black", fg="white")
text.pack(fill="both", expand=True)

error_occurred = False

while True:
    try:
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        disk = psutil.disk_usage('C:\\')
        disk_percent = disk.percent
        disk = psutil.disk_usage('C:\\')
        disk_percent = disk.percent
        bar_length = 20
        cpu_bar = int(cpu_percent / 100 * bar_length)
        memory_bar = int(memory_percent / 100 * bar_length)
        disk_bar = int(disk_percent / 100 * bar_length)
        text.delete("0.0", "end")
        text.insert("0.0", f"\n{'CPU:':<5} [{'|' * cpu_bar}{' ' * (bar_length - cpu_bar)}] {cpu_percent}%\n")
        text.insert("end", f"{'RAM:':<5} [{'|' * memory_bar}{' ' * (bar_length - memory_bar)}] {memory_percent}%\n")
        text.insert("end", f"{'Dysk:':<5} [{'|' * disk_bar}{' ' * (bar_length - disk_bar)}] {disk_percent}%\n")
        text.insert("end", "\n")
        text.see("end")
        root.update()
        if root.focus_get() == None: # Sprawdzenie, czy okno jest aktywne
            root.overrideredirect(False) # Pokazanie dekoracji okna
        else:
            time.sleep(2.0)
            root.overrideredirect(True) # Ukrycie dekoracji okna
        root.focus_force() # Ustawienie fokusu klawiatury na oknie
        time.sleep(0.3)
    except Exception as e:
        if not error_occurred:
            print(f"Error: {e}")
            error_occurred = True
            sys.exit()
