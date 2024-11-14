FROM ollama/ollama:latest

# pulls the model and starts ollama
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 11434

ENTRYPOINT ["sh"]
CMD ["start.sh"]
