from quart import Quart
from quart import render_template

from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random



app = Quart(__name__)


async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    resp.raise_for_status()
    pokemon = resp.json()
    return pokemon

async def get_pokemons():
    rand_list = [random.randint(1, 151) for _ in range(10)]
    pokemon_data = []
    async with httpx.AsyncClient() as client:
        tasks = [get_pokemon(client, f'https://pokeapi.co/api/v2/pokemon/{number}') for number in rand_list]
        results = await asyncio.gather(*tasks)
        for pokemon_json in results:
            pokemon_object = Pokemon(pokemon_json)
            pokemon_data.append(pokemon_object)
    return pokemon_data

@app.route('/')
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time - start_time} seconds")
    return await render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50002)
