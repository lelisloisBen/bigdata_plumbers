import json
import boto3
import random
import datetime

# IAM ROLE FOR KINESIS:  KinesisFirehoseServiceRole-mycsv-us-west-2-1599583279633

# kinesis = boto3.client('kinesis')

client = boto3.client(
    'kinesis',
    region_name='us-east-2',
    aws_access_key_id="AKIA4ESOEUICQDFJ4DKG",
    aws_secret_access_key="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"
)


def getReferrer():
    data = {}
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['EVENT_TIME'] = str_now
    data['TICKER'] = random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV'])
    price = random.random() * 100
    data['PRICE'] = round(price, 2)
    return data

while True:
        data = json.dumps(getReferrer())
        print(data)
        client.put_record(
                StreamName="myStream",
                Data=data)
 
