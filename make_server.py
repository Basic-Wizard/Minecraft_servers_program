#!/usr/bin/env python

import os
import requests

# Configuration
server_dir = 'test_servers/test_server_1'
server_jar_url = 'https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar'
server_jar_name = 'minecraft_server.jar'

# Ensure server directory exists
if not os.path.exists(server_dir):
    os.makedirs(server_dir)

# Download Minecraft server JAR
def download_server_jar(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("Minecraft server JAR downloaded.")

# Generate server.properties file
def generate_properties_file(path):
    default_properties = """#Minecraft server properties
spawn-protection=16
max-tick-time=60000
query.port=25565
generator-settings=
sync-chunk-writes=true
force-gamemode=false
allow-nether=true
enforce-whitelist=false
gamemode=survival
broadcast-console-to-ops=true
enable-query=false
player-idle-timeout=0
difficulty=easy
spawn-monsters=true
broadcast-rcon-to-ops=true
op-permission-level=4
pvp=true
snooper-enabled=true
level-type=default
hardcore=false
enable-command-block=false
max-players=20
network-compression-threshold=256
resource-pack-sha1=
max-world-size=29999984
function-permission-level=2
rcon.port=25575
server-port=25565
server-ip=
spawn-npcs=true
allow-flight=false
level-name=world
view-distance=10
resource-pack=
spawn-animals=true
white-list=false
rcon.password=
generate-structures=true
max-build-height=256
online-mode=true
level-seed=
use-native-transport=true
prevent-proxy-connections=false
enable-rcon=false
motd=A Minecraft Server"""
    with open(path, 'w') as file:
        file.write(default_properties)
    print("server.properties generated.")

# Accept EULA
def accept_eula(path):
    with open(path, 'w') as file:
        file.write("eula=true\n")
    print("EULA accepted.")

# Main function to setup Minecraft server
def setup_minecraft_server():
    # Download server JAR
    download_server_jar(server_jar_url, os.path.join(server_dir, server_jar_name))
    
    # Generate server.properties
    generate_properties_file(os.path.join(server_dir, 'server.properties'))
    
    # Accept EULA
    accept_eula(os.path.join(server_dir, 'eula.txt'))

if __name__ == '__main__':
    setup_minecraft_server()
