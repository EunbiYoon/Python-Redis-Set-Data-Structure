import redis
from time import sleep

client=redis.Redis(host='127.0.0.1', port=6379)

# demo the sets
client.sadd('pythonlist','value1','value2','value3','value4')
client.sadd('powershelllist','value4','value5','value6','value7')

#duplicate
print(client.sinter('pythonlist','powershelllist'))

#union
print(client.sunion('pythonlist','powershelllist'))

#number of list
print(client.scard('pythonlist'))
print(client.scard('powershelllist'))

