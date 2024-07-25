#!/bin/bash

# Function to add a user if they do not already exist
add_user() {
    local username=$1
    local password=$2

    # Check if the user already exists
    if id "$username" &>/dev/null; then
        echo "User $username already exists. Password will not be changed."
    else
        # Create the user with a home directory and append to student group
        sudo useradd -m -s /bin/bash -G student "$username"
        if [ $? -eq 0 ]; then
            echo "$username:$password" | sudo chpasswd
            echo "User $username has been created with the default password and added to student group."
        else
            echo "Failed to create user $username."
        fi
    fi
}

# Ensure the student group exists
if ! getent group student >/dev/null; then
    sudo groupadd student
fi

# Add users here
add_user "demo" "demo"