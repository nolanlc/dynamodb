########################################################
#
# Query Contacts by Group
#
# This program will scan Contacts table and filter out
# user specified group.  
#
########################################################
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr


def get_unique_attribute_list(dynamodb, table_name, attribute_name):
    unique_attribute_list = []
    table = dynamodb.Table(table_name)
    response = table.scan()
    Items = response['Items']
    for contact in Items:
        attribute = contact[attribute_name]
        if attribute not in unique_attribute_list:
            unique_attribute_list.append(attribute)

    return unique_attribute_list


########################################################################
#
# Main Program
#
########################################################################
region = "us-west-1"
dynamodb = boto3.resource('dynamodb', region_name=region)

table_name = "Contacts"
attribute_name = "group"
group_list = get_unique_attribute_list(dynamodb, table_name, attribute_name)

print(group_list)
group = input("Query which group? ")

table = dynamodb.Table('Contacts')
response = table.scan(
    FilterExpression=Attr("group").eq(group)
)


##################################################################
#Output email list to file
##################################################################
f= open('email_list','w')
f.write("Email list for group'"+group+"'\n\n")

Items = response['Items']
for contact in Items:
    email = contact['email']
    full_name = contact['full_name'] 
    group = contact['group']

    f.write(email+",\n")
    print(email +" "+full_name+" "+group)
    

