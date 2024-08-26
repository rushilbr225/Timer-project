
import json
import boto3

client = boto3.resource('dynamodb')
table = client.Table('timer')

def getItem(court, date):
  items = table.get_item(
    Key={
        'court': court,
        'date': date
        }
    )
  return items

def putItem(array,court, date):
  response = table.put_item(Item={
        'court': court,
        'date': date,
        'value': array
    })

def schedule(court, date, time, user):
  items = getItem(court, date)
  item = items['Item']['value']
  for x in item:
    if x['time'] == time:
        if x['User'] == 'AVAIL':
          x['User'] = user
          putItem(item,court,date)
          return True
        else:
          return False

def getArray():
  array = []
  with open("data.json", 'r') as f:
    array = json.load(f)
  return array  

def insertItem(court, date):
  items = getItem(court, date)
  if 'Item' in items:
    return items
  else :
    putItem(getArray(),court, date)
    return getItem(court, date)
    

def lambda_handler(event, context):
  court = 'court1'
  date = '24/09/2024'
  time = '09:10'
  user = 'rushil.br'
  return schedule(court,date, time, user)


  
  
