import requests
from os import environ
from dotenv import load_dotenv
from time import sleep

load_dotenv()

period = environ.get('GOOGLE_DOMAINS_HOSTNAME', 60 * 30)

def update():

    HOSTNAME = environ.get('GOOGLE_DOMAINS_HOSTNAME')
    USERNAME = environ.get('GOOGLE_DOMAINS_USERNAME')
    PASSWORD = environ.get('GOOGLE_DOMAINS_PASSWORD')

    url = f'https://{USERNAME}:{PASSWORD}@domains.google.com/nic/update'
    params = { 'hostname': HOSTNAME}

    response = requests.post(url, params=params)
    print(response.text)


update()