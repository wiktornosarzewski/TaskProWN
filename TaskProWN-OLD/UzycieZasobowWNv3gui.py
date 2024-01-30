import tkinter as tk
from colorama import init, Fore, Back, Style
import psutil
import time

init()

root = tk.Tk()
root.title("Wyniki")
root.geometry("400x300")

text = tk.Text(root, bg="black", fg="white")
text.pack(fill="both", expand=True)

while True:
    # CPU usage
    cpu_percent = psutil.cpu_percent()
    text.insert("end", f"Użycie CPU: {cpu_percent}%\n")

    # RAM usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    text.insert("end", f"Użycie RAM: {memory_percent}%\n")

    # Disk usage
    disk = psutil.disk_usage('C:\\')
    disk_percent = disk.percent
    text.insert("end", f"Użycie dysku C: {disk_percent}%\n")

    # Progress bar
    bar_length = 20
    cpu_bar = int(cpu_percent / 100 * bar_length)
    memory_bar = int(memory_percent / 100 * bar_length)
    disk_bar = int(disk_percent / 100 * bar_length)

    text.insert("end", f"{'CPU:':<5} [{'=' * cpu_bar}{' ' * (bar_length - cpu_bar)}] {cpu_percent}%\n")
    text.insert("end", f"{'RAM:':<5} [{'=' * memory_bar}{' ' * (bar_length - memory_bar)}] {memory_percent}%\n")
    text.insert("end", f"{'Dysk:':<5} [{'=' * disk_bar}{' ' * (bar_length - disk_bar)}] {disk_percent}%\n")

    text.insert("end", "\n")
    text.see("end")

    root.update()

    time.sleep(0.5)
