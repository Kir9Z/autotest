import requests 

host = 'https://api.pokemonbattle.me:9104'
token = '424c15b932b640bb5e72f39d9d886bfc'


response_kill = requests.post(f'{host}/pokemons/kill', json =  {
    'pokemon_id': '13258'
}, headers =  {
    'Content-Type' : 'application/json',
    'trainer_token' : token
})

print(response_kill.text)