# Stage 1: Pull the model
FROM ollama/ollama:latest as model-puller

# Start Ollama server in the background
RUN ollama serve > /dev/null 2>&1 & \
    sleep 5 && \
    ollama pull llama3 && \
    pkill ollama

# Stage 2: Final image
FROM ollama/ollama:latest

EXPOSE 11434

VOLUME /root/.ollama

# Copy the pulled model from the first stage
COPY --from=model-puller /root/.ollama /root/.ollama

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]