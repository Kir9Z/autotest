import requests 
import json

host = 'https://api.pokemonbattle.me:9104'
token = '424c15b932b640bb5e72f39d9d886bfc'


response_newpokemon = requests.post(f'{host}/pokemons', json =  {
    "name": "Черенок",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers =  {
    'Content-Type' : 'application/json',
    'trainer_token' : token
})



print(response_newpokemon.text)

pok_id = response_newpokemon.json()['id']

print (pok_id)

response_changename = requests.put(f'{host}/pokemons', json =  {
    "pokemon_id": pok_id,
    "name": "Шифер",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}, headers =  {
    'Content-Type' : 'application/json',
    'trainer_token' : token
})

print (response_changename.text)

response_getpokeball = requests.get(f'{host}/trainers/add_pokeball', json =  {
    "pokemon_id": pok_id,
}, headers =  {
    'Content-Type' : 'application/json',
    'trainer_token' : token
})

print(response_getpokeball.text)