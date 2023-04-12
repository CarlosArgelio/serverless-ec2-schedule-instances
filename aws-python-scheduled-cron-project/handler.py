import os
import datetime
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

region = os.environ['REGION']
instance = os.environ['INSTANCES']

ec2 = boto3.client('ec2', region_name=region)

def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    hour = event['time']
    hour = datetime.datetime.strptime(hour, "%H")

    if hour == os.environ['START']:
        ec2.start_instances(InstanceIds=instance)
        logger.info("The instances " + str(instance) + " started")
    
    elif hour == os.environ['END']:
        ec2.stop_instances(InstanceIds=instance)
        logger.info("The instances " + str(instance) + " stop")
    
    else:
        logger.info("Review code!")
