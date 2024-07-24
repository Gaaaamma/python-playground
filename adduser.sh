#!/bin/bash

usage() {
    echo "Usage: ./adduser.sh {container_name}"
    exit 1
}

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    usage
fi

CONTAINER_NAME=$1
ACCOUNT_SCRIPT=create_account.sh

docker cp $ACCOUNT_SCRIPT sandbox:/bin/$ACCOUNT_SCRIPT
docker exec -it $CONTAINER_NAME /bin/bash -c $ACCOUNT_SCRIPT