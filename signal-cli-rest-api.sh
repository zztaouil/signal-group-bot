#!/bin/bash

docker run -p 8080:8080 \
    -v $(pwd)/signal-cli-config:/home/.local/share/signal-cli \
    -e 'MODE=json-rpc' bbernhard/signal-cli-rest-api:latest