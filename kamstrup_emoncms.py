import requests
import random
import time


API_URL = 'https://emoncms.org/input/post.json?json='
API_KEY = '--api read write key here'

while True:
    data = random.random()*100
    data = str(int(data+200))
    r = requests.post(API_URL + '{power:' + data + '}&apikey=' + API_KEY, verify = False)
    print r
    time.sleep(9)
