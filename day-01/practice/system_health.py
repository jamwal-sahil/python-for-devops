import psutil


def check_system_health():
    cpu_threshold = int(input("Enter the CPU Usage Threshold"))
    disk_threshold = int(input("Enter the Disk Usage Threshold"))
    memory_threshold = int(input("Enter the Memory Threshold"))


    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU Usage %: ",current_cpu)
    current_disk = psutil.disk_usage('/')
    print("Current Disk Usage: ",current_disk)
    current_memory = psutil.virtual_memory()
    print("Current Memory Usage: ",current_memory)

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    else:
        print("CPU in Safe state...")
    
    if current_disk.percent > disk_threshold:
        print("Disk Usage Alert Email sent...")
    else:
        print("Disk Usage is within threshold...")

    if current_memory.percent > memory_threshold:
        print("Memory Usage Alert Email sent...")
    else:
        print("Memory Usage is within threshold...")

check_system_health()