import tkinter as tk
import psutil
import time
import sys

root = tk.Tk()
root.title("ProTask - Wiktor Nosarzewski")
root.geometry("280x90")
root.attributes('-topmost', True)
root.attributes('-alpha', 0.3) # Dodanie przezroczystości
root.overrideredirect(True) # Usunięcie dekoracji okna
root.geometry("+0+0") # Ustawienie pozycji okna na lewy górny róg ekranu

text = tk.Text(root, bg="black", fg="white")
text.pack(fill="both", expand=True)

error_occurred = False

def move_window(event):
    if event.keysym == 'F1':
        root.geometry("+0+0")
    elif event.keysym == 'F2':
        root.geometry(f"+{root.winfo_screenwidth()-root.winfo_width()}+0")
    elif event.keysym == 'F3':
        root.geometry("+0+"+str(root.winfo_screenheight()-root.winfo_height()))
    elif event.keysym == 'F4':
        root.geometry(f"+{root.winfo_screenwidth()-root.winfo_width()}+{root.winfo_screenheight()-root.winfo_height()}")
    elif event.keysym == 'F5':
        root.overrideredirect(False)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 1.0)
    elif event.keysym == 'F6':
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 0.5)
    elif event.keysym == 'F7':
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 0.7)
    elif event.keysym == 'F8':
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 1.0)

root.bind("<Key>", move_window)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"+0+{screen_height - 90}")
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
        time.sleep(0.3)
    except Exception as e:
        if not error_occurred:
            print(f"Error: {e}")
            error_occurred = True
            sys.exit()
