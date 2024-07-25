#!/bin/bash

usage() {
    echo "Usage: ./create_account.sh {container_name}"
    exit 1
}

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    usage
fi

CONTAINER_NAME=$1
ADD_USER_SCRIPT=adduser.sh

docker cp $ADD_USER_SCRIPT sandbox:/bin/$ADD_USER_SCRIPT
docker exec -it $CONTAINER_NAME /bin/bash -c $ADD_USER_SCRIPT