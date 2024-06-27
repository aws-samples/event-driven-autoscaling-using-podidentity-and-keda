FROM python:3.11
# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Create a non-root user and switch to it
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser


# Copy requirements and install dependencies
COPY --chown=appuser:appgroup requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY --chown=appuser:appgroup ./sqs_read_msg.py ./sqs_read_msg.py
USER appuser
# Specify the command to run the application
CMD ["python", "./sqs_read_msg.py"]
