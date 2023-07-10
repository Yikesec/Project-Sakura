#!/bin/sh

# Function to display ASCII sudo message
display_sudo_message() {
    echo "                                                                "
    echo "                                                                "
    echo "                                                                "
    echo "  /XXXXXX  /XX                       /XX       /XX   /XX    /XX"
    echo " /XX__  XX| XX                      | XX      |__/  | XX   | XX"
    echo "| XX  \ XX| XXXXXXX         /XXXXXXX| XXXXXXX  /XX /XXXXXX | XX"
    echo "| XX  | XX| XX__  XX       /XX_____/| XX__  XX| XX|_  XX_/ | XX"
    echo "| XX  | XX| XX  \ XX      |  XXXXXX | XX  \ XX| XX  | XX   |__/"
    echo "| XX  | XX| XX  | XX       \____  XX| XX  | XX| XX  | XX /XX   "
    echo "|  XXXXXX/| XX  | XX       /XXXXXXX/| XX  | XX| XX  |  XXXX//XX"
    echo " \______/ |__/  |__/      |_______/ |__/  |__/|__/   \___/ |__/"
    echo "                                                                "
    echo "                                                                "
    echo "                                                                "
    echo "Please run this script as sudo"
}

# Check if the script is run as sudo (root)
if [ "$EUID" -ne 0 ]; then
    display_sudo_message
    exit
fi

# Change the script's permissions
chmod 755 "$0"

# Change the permissions of the directory as a backup if chmod does not run the first time
chmod 755 /home/yikesec/Desktop/Project-Sakura-main/

adjust_console_size() {
    local cols=166
    local lines=27
    printf "\033[8;%d;%dt" "$lines" "$cols"
}

# Function to display ASCII warning message
display_warning() {
    echo " ___________________________________________________________ "
    echo "|                                                           |"
    echo "|  WARNING: This installation process may take a long time  |"
    echo "|___________________________________________________________|"
    echo ""
}

# Function to display error messages
display_error() {
    local error_message=$1
    echo "An error occurred: $error_message"
    echo "Please check your system configuration and try again."
}

# Adjust console size
adjust_console_size

# Title isn't supported in Unix-based systems like Linux or MacOS.
# You could add an echo statement as an alternative.

echo "Sakura Modules Installer /// V3.1"
clear

# Display warning message
display_warning

# Function to handle "Could not get lock" error
handle_lock_error() {
    local retries=10
    local delay=1

    for ((i=1; i<=retries; i++)); do
        echo "Waiting for cache lock... Retry $i"

        # Attempt to install python3-venv package
        sudo apt install python3-venv

        # Check if installation succeeded
        if [ $? -eq 0 ]; then
            return 0
        fi

        # Sleep for a delay before retrying
        sleep "$delay"
    done

    # Display error message if installation failed after retries
    display_error "Failed to install python3-venv package"
    exit 1
}

cat installertext.txt

# Check if python3-venv package is installed
if ! command -v python3-venv &> /dev/null; then
    echo "python3-venv package not found. Installing..."

    # Handle "Could not get lock" error
    handle_lock_error
fi

# Create a virtual environment
python3 -m venv sakura_venv || { display_error "Failed to create the virtual environment"; exit 1; }

# Activate the virtual environment
source sakura_venv/bin/activate || { display_error "Failed to activate the virtual environment"; exit 1; }

# Install the required packages inside the virtual environment
pip install -r requirements.txt || { display_error "Failed to install the required packages"; exit 1; }

cat textinstalled.txt

# Reset console size to default
tput reset

# Check if numpy and yarl failed to build wheels
if [ $? -ne 0 ]; then
    display_error "Failed to build one or more required packages (numpy, yarl)"
    echo "Please make sure all necessary dependencies are installed and try again."
    exit 1
fi

# Unix shell doesn't have a direct equivalent to `pause` in batch scripts
# You could use `read` to create a pause-like effect

read -n 1 -s -r -p "Press any key to continue"
