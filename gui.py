#!/usr/bin/env python

# Import necessary modules
import tkinter as tk  # Tkinter for GUI creation
from tkinter import messagebox, scrolledtext, simpledialog  # Additional widgets
import subprocess  # For running shell commands
import os  # For filesystem operations

# Function to create a new server
def create_server():
    # Prompt the user to enter a new server name
    server_name = simpledialog.askstring("Input", "Enter new server name:", parent=root)
    if server_name:  # If a server name was entered
        server_dir = f'servers/{server_name}'  # Construct the server directory path
        # URL to the Minecraft server JAR (constant in this case)
        server_jar_url = 'https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar'
        server_jar_name = 'minecraft_server.jar'  # Name for the server JAR file
        # Run the make_server.py script with the specified arguments to create the server
        subprocess.run([
    './make_server.py',
    '-dir', server_dir,
    '-url', server_jar_url,
    '-n', server_jar_name
], check=True)
        # Update the server list in the GUI
        update_server_list()

# Function to update the list of servers in the GUI
def update_server_list():
    server_listbox.delete(0, tk.END)  # Clear the current list
    # Iterate over directories in the 'servers' folder
    for server_dir in os.listdir('servers'):
        server_listbox.insert(tk.END, server_dir)  # Add each server directory to the listbox

# Function to start a selected server
def start_server():
    selected_server = server_listbox.get(tk.ANCHOR)  # Get the currently selected server from the listbox
    if selected_server:  # If a server is selected
        # Run the open_server.sh script with 'start' argument in the selected server's directory
        subprocess.run(['./open_server.sh', 'start', selected_server], cwd=f'servers/{selected_server}')

# Function to stop a selected server
def stop_server():
    selected_server = server_listbox.get(tk.ANCHOR)  # Get the currently selected server
    if selected_server:  # If a server is selected
        # Run the open_server.sh script with 'close' argument in the selected server's directory
        subprocess.run(['./open_server.sh', 'close', selected_server], cwd=f'servers/{selected_server}')

# Function to restart a selected server
def restart_server():
    selected_server = server_listbox.get(tk.ANCHOR)  # Get the currently selected server
    if selected_server:  # If a server is selected
        # Run the restart_server.sh script with 'start' argument in the selected server's directory
        subprocess.run(['./restart_server.sh', 'start', selected_server], cwd=f'servers/{selected_server}')

import tkinter as tk
from tkinter import simpledialog, messagebox, font as tkfont  # Import additional modules as needed

# Adjust these values as needed for your specific requirements
window_width = 600
window_height = 400
button_font_size = 16  # Font size for buttons
listbox_font_size = 16  # Font size for the listbox

# Function definitions (create_server, update_server_list, start_server, stop_server, restart_server) go here

# Initialize the main window (root) of the GUI
root = tk.Tk()
root.title("Minecraft Server Manager")  # Set the window title

# Set the window size
root.geometry(f'{window_width}x{window_height}')

# Define font styles for widgets
button_font = tkfont.Font(size=button_font_size)
listbox_font = tkfont.Font(size=listbox_font_size)

# Create and pack the "Create New Server" button into the GUI
create_server_button = tk.Button(root, text="Create New Server", command=create_server, font=button_font)
create_server_button.pack(pady=10)  # Add some padding for better spacing

# Create and pack the listbox that will display the list of servers
server_listbox = tk.Listbox(root, font=listbox_font)
server_listbox.pack(pady=10)  # Add some padding for better spacing

# Create and pack the "Start Server" button
start_button = tk.Button(root, text="Start Server", command=start_server, font=button_font)
start_button.pack(pady=5)  # Adjust padding as needed

# Create and pack the "Stop Server" button
stop_button = tk.Button(root, text="Stop Server", command=stop_server, font=button_font)
stop_button.pack(pady=5)  # Adjust padding as needed

# Create and pack the "Restart Server" button
restart_button = tk.Button(root, text="Restart Server", command=restart_server, font=button_font)
restart_button.pack(pady=5)  # Adjust padding as needed

# Start the Tkinter event loop
root.mainloop()


