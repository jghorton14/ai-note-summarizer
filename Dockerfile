# Use the latest Ubuntu image
FROM ubuntu:latest

# Set the working directory to /usr/local/bin
WORKDIR /usr/local/bin

# Copy the startup script into the container
COPY ollama-install.sh /usr/local/bin/
COPY startup.sh /usr/local/bin/

# Make the script executable
RUN chmod +x ollama-install.sh
RUN chmod +x startup.sh

EXPOSE 11434

# Install curl
RUN apt-get update && apt-get install -y curl

# Run the script and then keep the container running
CMD ["sh", "-c", "./ollama-install.sh && ./startup.sh"]

# docker build -t ollama-intro .
# docker run -it ollama-intro

# docker run -it -p 11434:11434 ollama-intro
