import requests
from time import sleep
import config_s
from playsound import playsound as unix_sound
from winsound import SND_FILENAME,PlaySound
import platform
from configs import PASSWORD

### asdf



file = 'files/napalm_death.wav' #Input sound file 
key = config_s.key #using AlphaVantage Bitcoin exchange rate API on sepate module config_s
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={key}'


request = requests.get(url).json()

value = float(request["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

while True:
    request = requests.get(url).json()
    value_new = float(request["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    if value == value_new:
        value_new = float(request["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        print(f'No changes - previous {value} - new {value_new}')
        sleep(15)
        
    elif value > value_new:
        if platform.system() == 'Windows':
            PlaySound(file,SND_FILENAME)
        else:
            unix_sound(file)
       
        print(f'Music! - previous {value} - new {value_new}')
        sleep(15)

    else:
        print(f'still looking - previous {value} - new {value_new}')
        sleep(15)

    request = requests.get(url).json()
    value = float(request["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    sleep(5)
        




