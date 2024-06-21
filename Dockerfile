FROM python:3.11
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./sqs_read_msg.py ./sqs_read_msg.py
CMD ["/bin/sh", "-c", "python ./sqs_read_msg.py"]
