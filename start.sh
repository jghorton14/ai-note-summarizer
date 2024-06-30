#!/bin/sh

# Start Ollama with CPU only on port 11434
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Wait for Ollama to start
sleep 10

# Run llama3 model
docker exec -it ollama ollama run llama3

# Keep the container running
tail -f /dev/null