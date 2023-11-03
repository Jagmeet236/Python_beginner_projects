#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage

disk_usage = check_disk_usage("/")
cpu_usage = check_cpu_usage()

print(f"Disk Usage: {disk_usage}%")
print(f"CPU Usage: {cpu_usage}%")

if disk_usage > 20 and cpu_usage < 75:
    print("Everything is okay!")
else:
    print("Error!")
