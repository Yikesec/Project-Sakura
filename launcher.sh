#!/bin/sh

# Display a loading message
echo "System is initializing. Please stand by."

# Display an animated loading icon
for i in $(seq 1 5)
do
  printf "."  # printf does not add a newline character at the end like echo does
  sleep 1
done
printf "\n"

# Run the Python script
python3 main.py

# Check for errors
if [ $? -ne 0 ]
then
  # If the Python script exits with a non-zero status code, print an error message
  echo "An unexpected error occurred while launching the program. If you have modified any part of the source code, please revert to the original state. If the problem persists or if you wish to suggest or add features to the repository/selfbot, kindly reach out to Kobayashi for support."
fi

# Pause and wait for user input before exiting
read -n 1 -s -r -p "Press any key to conclude the program execution. Project Sakura could not be launched."
