#!/bin/bash

# starts ollama service
ollama serve &

# waits for service start
sleep 5

# pulls the llama3.2 model
ollama pull llama3.2

# keeps the container running
wait
