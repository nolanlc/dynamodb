########################################################
#
# Create Contacts table
#
########################################################

import boto3

region = "us-west-1"
dynamodb = boto3.resource('dynamodb', region_name=region)

table = dynamodb.create_table(
    TableName='Contacts',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH' #Partition key
        },
        {
            'AttributeName': 'group',
            'KeyType': 'RANGE' #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'group',
            'AttributeType': 'S'
        }
   ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)
print("Table tatus:", table.table_status)


