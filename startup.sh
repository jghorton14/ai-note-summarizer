#!/bin/bash

echo "before starting ollama"

ollama serve > output.log &

ps -ef

ollama ps 

ollama pull llama3:latest

ollama show llama3
