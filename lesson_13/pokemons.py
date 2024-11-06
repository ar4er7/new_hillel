import random
import sys
import time
from pprint import pprint as print

import requests

POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2/berry"


def fetch_pokemons(_id: int) -> dict:
    response: requests.Response = requests.get(url=f"{POKEAPI_BASE_URL}/{_id}")
    return response.json()


def main():
    try:
        pokemons_number: int = int(sys.argv[1])
    except IndexError:
        print("please enter the number of pokemons to be fetched")
    except ValueError:
        print("only integers allowed")

    results: list[dict] = []
    for _ in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        pokemon = fetch_pokemons(_id=random_id)
        results.append(pokemon)
    print(len(results))


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f"{time.perf_counter() - start}")
