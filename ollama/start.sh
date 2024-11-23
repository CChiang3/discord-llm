#!/bin/bash

# starts ollama service
ollama serve &

# waits for service start
sleep 5

# pulls the llama3.2 model
ollama pull qwen2.5:1.5b

# keeps the container running
wait
