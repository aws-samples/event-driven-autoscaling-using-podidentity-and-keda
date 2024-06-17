#!/usr/bin/env python3

import argparse
import logging
import sys
import uuid
import json
from random import randint
from time import sleep

import boto3
from botocore.exceptions import ClientError

# Example Command
# Full Command : python ./sqs_send_msg.py -q event-messages-queue -i 10 -m '{"num": "10"}'
# Short Command : python ./sqs_send_msg.py
AWS_REGION = boto3.session.Session().region_name
parser = argparse.ArgumentParser()
parser.add_argument("--queue-name", "-q", default="event-messages-queue", help="SQS queue name")
parser.add_argument("--interval", "-i", default=3, help="timer interval", type=float)
parser.add_argument("--message", "-m", help="message to send")
parser.add_argument("--log", "-l", default="INFO", help="logging level")
args = parser.parse_args()

if args.log:
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=args.log)
else:
    parser.print_help(sys.stderr) 

sqs = boto3.client("sqs", region_name=AWS_REGION)

try:
    logging.info(f"Getting queue URL for queue: {args.queue_name}")
    response = sqs.get_queue_url(QueueName=args.queue_name)
except ClientError as e:
    logging.error(e)
    exit(1)

queue_url = response["QueueUrl"]
logging.info(f"Queue URL: {queue_url}")

i = 0

while True:
    try:
        i = randint(1, 38)
        _t = randint(1, 20)
        if _t == 7:
            i = 40

        # i =  i + 1
        # if i >= 25:
        #     break

        _temp = {"num": str(i)}
        message = json.dumps(_temp)
        logging.info("Sending message: " + message)
        response = sqs.send_message(QueueUrl=queue_url, MessageBody=message)
        logging.info("MessageId: " + response["MessageId"])
        sleep(args.interval)
    except ClientError as e:
        logging.error(e)
        exit(1)
