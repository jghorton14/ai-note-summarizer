#!/bin/bash
set -e

echo "Starting Ollama server..."
ollama serve > ollama.log &
sleep 5  # Give the server a moment to start

echo "Running llama3 model..."
exec ollama run llama3