#!/bin/bash

# # Define the custom screen socket directory
# export SCREENDIR=../socketdir

# Configuration
SERVER_DIRECTORY="servers/test_gui"
SERVER_JAR="minecraft_server.jar"
SCREEN_NAME="MinecraftServer" # The name of the screen session used to run the server in the background.
MEMORY="2048M" # The amount of memory allocated to the Minecraft server. Adjust as necessary.

# Change directory to the server directory. This ensures that any relative file paths are correctly interpreted from the server directory.
cd "$SERVER_DIRECTORY"

# start_server function: Attempts to start the Minecraft server in a new screen session if it's not already running.
start_server() {
    # Checks if a screen session with the name $SCREEN_NAME already exists.
    if screen -list | grep -q "\.$SCREEN_NAME"; then
        echo "Server is already running!" # If the server is already running, print a message and do nothing.
    else
        echo "Starting server..."
        # Starts the server in a detached screen session with the specified name and memory allocation.
        screen -dmS $SCREEN_NAME java -Xmx$MEMORY -Xms$MEMORY -jar $SERVER_JAR #nogui
        echo "Server started." # Confirms that the server has been started.
    fi
}

# stop_server function: Gracefully stops the Minecraft server if it's running.
stop_server() {
    # Checks if a screen session with the name $SCREEN_NAME exists.
    if screen -list | grep -q "\.$SCREEN_NAME"; then
        echo "Stopping server..."
        # Sends the "stop" command to the server console to gracefully stop the server.
        screen -S $SCREEN_NAME -X stuff "stop^M"
        sleep 10 # Waits for 10 seconds to allow the server to shut down properly.
        echo "Server stopped." # Confirms that the server has been stopped.
    else
        echo "Server is not running!" # If the server is not running, print a message.
    fi
}

# restart_server function: Restarts the Minecraft server by first stopping it and then starting it again.
restart_server() {
    echo "Restarting server..."
    stop_server # Calls stop_server function to stop the server.
    start_server # Calls start_server function to start the server.
}

# Main section: Processes the script's command-line argument to determine the action to take (start, stop, restart).
case "$1" in
    start)
        start_server # If the argument is "start", call the start_server function.
        ;;
    stop)
        stop_server # If the argument is "stop", call the stop_server function.
        ;;
    restart)
        restart_server # If the argument is "restart", call the restart_server function.
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}" # If an unrecognized argument is provided, print usage information.
        exit 1 # Exit the script with an error status.
        ;;
esac