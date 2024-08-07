# from pypokemon.pokemon import Pokemon
# import asyncio
# import httpx
# import time
# import random

# async def get_pokemon(client, url):
#     print(f"{time.ctime()} - get {url}")
#     resp = await client.get(url)
#     pokemon = resp.json()

#     return Pokemon(pokemon)

# async def get_pokemons():
#     async with httpx.AsyncClient() as client:
#         tasks = []
#         rand_list=[]
#         for i in range(5):
#             rand_list.append(random.randint(1,151))

#         for number in rand_list:
#             url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#             tasks.append(asyncio.create_task(get_pokemon(client, url)))

#         pokemons = await asyncio.gather(*tasks)
#         return pokemons

# async def index():
#     start_time = time.perf_counter()
#     pokemons = await get_pokemons()
#     end_time = time.perf_counter()
#     print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

# if __name__ == '__main__':
#    asyncio.run(index()) 

from quart import Quart, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon  # Assuming this is the correct import for the Pokemon class

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
    app.run(debug=True, port=5002)
