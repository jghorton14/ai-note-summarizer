FROM ollama-intro:latest

EXPOSE 11434

# Install curl
RUN apt-get update && apt-get upgrade

# Run the script and then keep the container running
CMD ["ollama serve > ollama.log 2>&1"]

# docker build -t ollama-custom-llama3 .
# docker run -it ollama-custom-llama3

# docker run -it -p 11434:11434 ollama-custom-llama3