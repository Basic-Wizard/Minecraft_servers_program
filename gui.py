#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import subprocess
import os

def create_server():
    server_name = simpledialog.askstring("Input", "Enter new server name:",
                                         parent=root)
    if server_name:
        server_dir = f'servers/{server_name}'
        server_jar_url = 'https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar'
        server_jar_name = 'minecraft_server.jar'
        # Assuming make_server.py can be modified to accept command line arguments
        subprocess.run(['python', 'make_server.py', server_dir, server_jar_url, server_jar_name], check=True)
        update_server_list()

def update_server_list():
    server_listbox.delete(0, tk.END)  # Clear the listbox
    for server_dir in os.listdir('servers'):
        server_listbox.insert(tk.END, server_dir)

def start_server():
    selected_server = server_listbox.get(tk.ANCHOR)
    if selected_server:
        subprocess.run(['./open_server.sh', 'start', selected_server], cwd=f'servers/{selected_server}')

def stop_server():
    selected_server = server_listbox.get(tk.ANCHOR)
    if selected_server:
        subprocess.run(['./open_server.sh', 'close', selected_server], cwd=f'servers/{selected_server}')

def restart_server():
    selected_server = server_listbox.get(tk.ANCHOR)
    if selected_server:
        subprocess.run(['./restart_server.sh', 'start', selected_server], cwd=f'servers/{selected_server}')

root = tk.Tk()
root.title("Minecraft Server Manager")

# Server creation
create_server_button = tk.Button(root, text="Create New Server", command=create_server)
create_server_button.pack()

# Server list
server_listbox = tk.Listbox(root)
server_listbox.pack()
update_server_list()  # Populate the list on startup

# Server control buttons
start_button = tk.Button(root, text="Start Server", command=start_server)
start_button.pack()

stop_button = tk.Button(root, text="Stop Server", command=stop_server)
stop_button.pack()

restart_button = tk.Button(root, text="Restart Server", command=restart_server)
restart_button.pack()

root.mainloop()
