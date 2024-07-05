# Stage 1: Pull the model (if not already present)
FROM ollama/ollama:latest as model-puller

# Start Ollama server in the background and pull the model if not present
RUN ollama serve > /dev/null 2>&1 & \
    sleep 5 && \
    if ! ollama list | grep -q llama3; then \
        ollama pull llama3; \
    else \
        echo "llama3 model already present, skipping pull"; \
    fi && \
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