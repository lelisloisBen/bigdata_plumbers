import boto3
import requests
from json import dumps
import json 
import os

access_key_id = os.environ['AWS_ACCESS']
secret_key = os.environ['AWS_SECRET']
rapid_yelp_key = os.environ['YELP_KEY']


client = boto3.client(
    'kinesis',
    region_name='us-east-2',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_key
)

myheaders = {
   	"x-rapidapi-host": "yelp-com.p.rapidapi.com",
	"x-rapidapi-key": rapid_yelp_key,
	"useQueryString": 'true'
}

x= requests.get('https://yelp-com.p.rapidapi.com/business/DAiqwrmv19Uv-I1bOoAJCQ', headers=myheaders)
t = x.json()
print(t)


client.put_record(StreamName='yelp_FES', Data=json.dumps(t).encode('utf-8'), PartitionKey='1')

    
