import requests
import json

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
data = []

def get_params(b,e,n):
    response = requests.get(b+e+f'?page={n}')
    return response.json()

def get_response(b,e,n) -> list:
    response = requests.get(b+e+f'?page={n}')
    output = response.json()
    return output['results']

def get_num_pages(response):
    print(f'There are {response['info']['pages']} pages.')
    return response['info']['pages']

def clear_data():
    with open('saves/character_data.json', mode='w') as f:
        f.close()

def save_data(d):
    with open('saves/character_data.json', mode='a') as f:
        j = json.dumps(d)
        json.dump(j,f,indent=3)

def load_data():
    with open('saves/character_data.json',mode='r') as f:
        return json.loads(json.load(f))

num_pages = get_num_pages(get_params(baseurl,endpoint,1))

for i in range(1):
    for n in get_response(baseurl,endpoint,i): #calls save_data i times
        data.append(n)
    print(f'Page {i} written.')

clear_data()
save_data(data)
var = load_data()