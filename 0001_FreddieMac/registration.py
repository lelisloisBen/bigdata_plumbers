import requests
import json 
# from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

# auth = BotoAWSRequestsAuth(
#     aws_host="i0tpt9ahrl.execute-api.us-east-1.amazonaws.com",
#     aws_region="us-east-1",
#     aws_service="execute-api"
# )

myheaders = {
   	"x-api-key": "tMIzS0ANqu4Y3qx5CzoSb7upt4g8Q7hX9WYGDFls",
	"Content-Type": "application/json"
}

body = {
	"name": "lss_app_byol_1",
	"active": "true",
	"prefixKey": "sf/lss",
	"sourceSchemaDb": "demodb",
	"sourceSchemaGlue": [{
			"name": "Region",
			"type": "string"
		},
		{
			"name": "Country",
			"type": "string"
		},
		{
			"name": "ItemType",
			"type": "string"
		},
		{
			"name": "SalesChannel",
			"type": "string"
		},
		{
			"name": "OrderPriority",
			"type": "string"
		},
		{
			"name": "OrderDate",
			"type": "string"
		},
		{
			"name": "OrderID",
			"type": "int"
		},
		{
			"name": "ShipDate",
			"type": "string"
		},
		{
			"name": "UnitsSold",
			"type": "string"
		},
		{
			"name": "UnitPrice",
			"type": "string"
		},
		{
			"name": "UnitCost",
			"type": "string"
		},
		{
			"name": "TotalRevenue",
			"type": "string"
		},
		{
			"name": "TotalCost",
			"type": "string"
		},
		{
			"name": "TotalProfit",
			"type": "string"
		}
	],
	"destinationSchemaDb": "schemadb",
	"destinationSchemaGlue": [{
			"name": "Region",
			"type": "string"
		},
		{
			"name": "Country",
			"type": "string"
		},
		{
			"name": "ItemType",
			"type": "string"
		},
		{
			"name": "SalesChannel",
			"type": "string"
		},
		{
			"name": "OrderPriority",
			"type": "string"
		},
		{
			"name": "OrderDate",
			"type": "string"
		},
		{
			"name": "OrderID",
			"type": "int"
		},
		{
			"name": "ShipDate",
			"type": "string"
		},
		{
			"name": "UnitsSold",
			"type": "string"
		},
		{
			"name": "UnitPrice",
			"type": "string"
		},
		{
			"name": "UnitCost",
			"type": "string"
		},
		{
			"name": "TotalRevenue",
			"type": "string"
		},
		{
			"name": "TotalCost",
			"type": "string"
		},
		{
			"name": "TotalProfit",
			"type": "string"
		},
		{
			"name": "edptimestamp",
			"type": "string"
		}
	],
	"dataQuality": {
		"className": "",
		"file": "s3://freddie-mac-sandbox-config/spark/byol/BYOL_innerJoinSpark.py",
		"sourceFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": "true"
		},
		"destinationFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": "true"
		}
	},
	"transform": {
		"className": "",
		"file": "s3://freddie-mac-sandbox-config/spark/byol/BYOL_innerJoinSpark.py",
		"sourceFileAttributes": {
			"type": "csv",
			"delimiter": "|",
			"header": "true"
		},
		"keyFields": ["OrderID"],
		"partitionBy": ["OrderDate"],
		"useDelta": "true",
		"useHudi": "false"
	}
}


r = requests.post('https://i0tpt9ahrl.execute-api.us-east-1.amazonaws.com/dev/dataset', headers=myheaders, body=body)
t = r.json()
print(t)
# x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=myheaders)
# t = x.json()
# print(t)