import tkinter as tk
from colorama import init, Fore, Back, Style
import psutil
import time

init()

root = tk.Tk()
root.title("Wyniki")
root.geometry("800x600")#400x300

text = tk.Text(root, bg="black", fg="white", font=("Courier", 15))
text.pack(fill="both", expand=True)

while True:
    # CPU usage
    cpu_percent = psutil.cpu_percent()
    text.delete("1.0", "2.0")
    if cpu_percent < 25:
        text.insert("1.0", f"Użycie CPU: {cpu_percent}%", Fore.GREEN)
    elif cpu_percent < 50:
        text.insert("1.0", f"Użycie CPU: {cpu_percent}%", Fore.YELLOW)
    elif cpu_percent < 75:
        text.insert("1.0", f"Użycie CPU: {cpu_percent}%", Fore.LIGHTMAGENTA_EX)
    else:
        text.insert("1.0", f"Użycie CPU: {cpu_percent}%", Fore.RED)

    # RAM usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    text.delete("2.0", "3.0")
    if memory_percent < 25:
        text.insert("2.0", f"Użycie RAM: {memory_percent}%", Fore.GREEN)
    elif memory_percent < 50:
        text.insert("2.0", f"Użycie RAM: {memory_percent}%", Fore.YELLOW)
    elif memory_percent < 75:
        text.insert("2.0", f"Użycie RAM: {memory_percent}%", Fore.LIGHTMAGENTA_EX)
    else:
        text.insert("2.0", f"Użycie RAM: {memory_percent}%", Fore.RED)

    # Disk usage
    disk = psutil.disk_usage('C:\\')
    disk_percent = disk.percent
    text.delete("3.0", "4.0")
    if disk_percent < 25:
        text.insert("3.0", f"Użycie dysku C: {disk_percent:.0f}%", Fore.GREEN)
    elif disk_percent < 50:
        text.insert("3.0", f"Użycie dysku C: {disk_percent:.0f}%", Fore.YELLOW)
    elif disk_percent < 75:
        text.insert("3.0", f"Użycie dysku C: {disk_percent:.0f}%", Fore.LIGHTMAGENTA_EX)
    else:
        text.insert("3.0", f"Użycie dysku C: {disk_percent:.0f}%", Fore.RED)

    # Progress bar
    bar_length = 40
    cpu_bar = int(cpu_percent / 100 * bar_length)
    memory_bar = int(memory_percent / 100 * bar_length)
    disk_bar = int(disk_percent / 100 * bar_length)

    text.delete("4.0", "end")
    text.insert("4.0", f"{'CPU:':<5} [{'=' * cpu_bar}{' ' * (bar_length - cpu_bar)}] {cpu_percent}%\n")
    text.insert("end", f"{'RAM:':<5} [{'=' * memory_bar}{' ' * (bar_length - memory_bar)}] {memory_percent}%\n")
    text.insert("end", f"{'Dysk:':<5} [{'=' * disk_bar}{' ' * (bar_length - disk_bar)}] {disk_percent:.0f}%\n")

    text.insert("end", "\n")
    text.see("end")

    root.update()

    time.sleep(0.5)
