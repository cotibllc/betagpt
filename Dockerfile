FROM python:3.9-slim

# Set environment variables
#ENV ANTHROPIC_API_KEY=your_anthropic_api_key
#ENV OPENAI_API_KEY=your_openai_api_key
#ENV GEMINI_API_KEY=your_gemini_api_key

# Install required packages
RUN pip install flask requests

# Create app directory
WORKDIR F:\Projects\githubprojects\BetaGPT

# Copy application files
COPY app.py .
COPY templates templates/

# Expose port
EXPOSE 443

# Run the application
CMD ["python", "app.py"]