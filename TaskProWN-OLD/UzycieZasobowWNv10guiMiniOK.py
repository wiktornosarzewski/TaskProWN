import tkinter as tk
import psutil
import time

root = tk.Tk()
root.title("Pro TaskManager by Wiktor Nosarzewski")
root.geometry("280x140") #400x300
root.attributes('-topmost', True)

text = tk.Text(root, bg="black", fg="white")
text.pack(fill="both", expand=True)

while True:
    # CPU usage
    cpu_percent = psutil.cpu_percent()
    text.delete("1.0", "2.0")
    text.insert("1.0", f"Użycie CPU: {cpu_percent}%\n")

    # RAM usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    text.delete("2.0", "3.0")
    text.insert("2.0", f"Użycie RAM: {memory_percent}%\n")

    # Disk usage
    disk = psutil.disk_usage('C:\\')
    disk_percent = disk.percent
    text.delete("3.0", "4.0")
    text.insert("3.0", f"Użycie dysku C: {disk_percent}%\n")

    disk = psutil.disk_usage('C:\\')
    disk_percent = disk.percent
    text.delete("3.0", "4.0")
    text.insert("3.0", f"Wolne miejsce na dysku C: {round(100-disk_percent)}%\n")

    # Progress bar
    bar_length = 20
    cpu_bar = int(cpu_percent / 100 * bar_length)
    memory_bar = int(memory_percent / 100 * bar_length)
    disk_bar = int(disk_percent / 100 * bar_length)

    text.delete("4.0", "end")
    text.insert("4.0", f"\n{'CPU:':<5} [{'|' * cpu_bar}{' ' * (bar_length - cpu_bar)}] {cpu_percent}%\n")
    text.insert("end", f"{'RAM:':<5} [{'|' * memory_bar}{' ' * (bar_length - memory_bar)}] {memory_percent}%\n")
    text.insert("end", f"{'Dysk:':<5} [{'|' * disk_bar}{' ' * (bar_length - disk_bar)}] {disk_percent}%\n")

    text.insert("end", "\n")
    text.see("end")

    root.update()

    time.sleep(0.3) #0.5
