#!/usr/bin/env python3
try:
    import logging
    import time
    import datetime
    import boto3
    import json
    from botocore.exceptions import ClientError

    print("All imports ok ...")
except Exception as e:
    print("Error Imports : {} ".format(e))

AWS_REGION = boto3.session.Session().region_name

def fib_v1(n):
    return n if n == 0 or n == 1 else fib_v1(n - 1) + fib_v1(n - 2)

QUEUE_NAME = "event-messages-queue"

logging.basicConfig(format="[%(levelname)s] %(message)s", level="INFO")
sqs = boto3.client("sqs", region_name=AWS_REGION)

try:
    logging.info(f"Getting queue URL for queue: {QUEUE_NAME}")
    response = sqs.get_queue_url(QueueName=QUEUE_NAME)
except ClientError as e:
    logging.error(e)
    exit(1)

queue_url = response["QueueUrl"]
logging.info(f"Queue URL: {queue_url}")
logging.info("Receiving messages from queue...")

while True:
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=3)
    
    if "Messages" in messages:
        for message in messages["Messages"]:
            try:
                logging.info(f'Message body: {message["Body"]}')
                _temp = json.loads(message["Body"])
                fib_number = int(_temp["num"])

                # Generate Fibonacci Series
                lst = []
                start = datetime.datetime.now()
                for i in range(fib_number):
                    lst.append(fib_v1(i))
                end = datetime.datetime.now()
                logging.info("V1 --- {0} > {1} >>> Time: {2}".format(fib_number, lst, end - start))

                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"])
            except:
                logging.error(f'Message Body is not in JSON format {message["Body"]}')
            finally:
                continue

    else:
        logging.info("Queue is now empty")
        time.sleep(5)