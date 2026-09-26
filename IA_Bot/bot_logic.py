import random
import os
import requests

#senha aleatória
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

#emoji aleatório
def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923","\U0001F60E","\U0001F525"]
    return random.choice(emodji)

#cara ou coroa
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "cara"
    else:
        return "coroa"
#imagem aleatorio
def get_duck_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']