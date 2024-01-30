import psutil
import os
import time

def print_usage():
    # CPU usage
    cpu_percent = psutil.cpu_percent()
    print(f"Użycie CPU: {cpu_percent}%", end="\r")

    # RAM usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print(f"Użycie RAM: {memory_percent}%", end="\r")

    # Disk usage
    disk = psutil.disk_usage('C:\\')
    disk_percent = disk.percent
    print(f"Użycie dysku C: {disk_percent}%", end="\r")

    # Progress bar
    bar_length = 20
    cpu_bar = int(cpu_percent / 100 * bar_length)
    memory_bar = int(memory_percent / 100 * bar_length)
    disk_bar = int(disk_percent / 100 * bar_length)

    print(f"{'CPU:':<5} [{'=' * cpu_bar}{' ' * (bar_length - cpu_bar)}] {cpu_percent}%", end="\r")
    print(f"{'RAM:':<5} [{'=' * memory_bar}{' ' * (bar_length - memory_bar)}] {memory_percent}%", end="\r")
    print(f"{'Dysk:':<5} [{'=' * disk_bar}{' ' * (bar_length - disk_bar)}] {disk_percent}%", end="\r")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_usage()
    time.sleep(0.5)
