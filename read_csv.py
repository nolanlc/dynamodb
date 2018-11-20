
import boto3


#group = input("Group type?: ")
#filename = input("Filename? ")

#group = 'Intern2018'
#filename = 'apapainterns2018.csv'

group = 'clf'
filename = 'clf.csv'

region = "us-west-1"
dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table("Contacts")


file = open(filename,'r')
line_count = 0
for line in file:
    tokens = line.split(',') #returns a list of tokens
    line_count = line_count + 1

    if line_count == 1:
        attribute_list = tokens
        #print (attribute_list)

    else:
        column_num = 0
        
        email = "UNKNOWN"
        full_name = "UNKNOWN"
        phone = "UNKNOWN"
        city = "UNKNOWN"

        for token in tokens:
            if column_num < len(attribute_list):
                attribute_name = attribute_list[column_num]
                if (token != ''):
                    if (attribute_name.upper() == 'EMAIL'):
                        email = token
                    elif (attribute_name.upper().count('NAME')>0):
                        full_name = token
                    elif (attribute_name.upper().count('PHONE') > 0):
                        phone = token
                    elif (attribute_name.upper().count('CITY') > 0):
                        city = token

            print (attribute_name + ": " + token)
            column_num = column_num + 1

        print ("email: "+email)
        print ("group: "+group)
        print ("full_name: "+full_name)
        print ("phone: "+phone)
        print ("city: "+city)
        print("\n")

        if (email != 'UNKNOWN'):
            table.put_item(
                Item={    
                'email' : email,
                'group' : group,
                'full_name' : full_name,
                'phone' : phone,
                'city' : city
                }
            )
        
   

