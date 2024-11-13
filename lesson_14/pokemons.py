import asyncio
import random
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint as print
from threading import Thread
from time import perf_counter
from typing import Coroutine

import httpx
import requests

POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2/berry"


def fetch_pokemons(_id: int) -> dict:
    response: requests.Response = requests.get(url=f"{POKEAPI_BASE_URL}/{_id}")

    if response.status_code != 200:
        print(f"Error: {response.status_code} | {response.text} | {_id=}")
        return {}
    else:
        print(response.status_code)
        return response.json()


def main_treads(pokemons_number: int):
    threads = []
    for i in range(pokemons_number):
        threads.append(Thread(target=fetch_pokemons, args=(random.randint(1, 50),)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main_threads_pool(pokemons_number: int):
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=pokemons_number) as executor:
        futures = []
        for i in range(pokemons_number):
            futures.append(executor.submit(fetch_pokemons, random.randint(1, 50)))

        for future in as_completed(futures):
            results.append(future.result())

    print(f"fetched {len(results)} pokemons")


def main_sync(pokemons_number: int):
    results: list[dict] = []
    for _ in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        pokemon = fetch_pokemons(_id=random_id)
        results.append(pokemon)

    return results


async def main_async(pokemons_number: int):
    # tasks = [
    #     asyncio.to_thread(fetch_pokemons, _id= random.randint(1, 50))
    #     for _ in range(pokemons_number)
    # ]
    async def get_with_httpx(url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            print(response.status_code)
            return response.status_code

    tasks: list[Coroutine] = [
        get_with_httpx(url=f"{POKEAPI_BASE_URL}/{random.randint(1,50)}")
        for i in range(pokemons_number)
    ]

    results = await asyncio.gather(*tasks)
    return results


def main():
    try:
        runtype: str = sys.argv[1]
        pokemons_number: int = int(sys.argv[2])
    except IndexError:
        print("please enter the number of pokemons to be fetched")
    except ValueError:
        print("only integers allowed")

    start = perf_counter()
    if runtype == "sync":
        main_sync(pokemons_number)
    elif runtype == "threads":
        main_treads(pokemons_number)
    elif runtype == "async":
        asyncio.run(main_async(pokemons_number))
    else:
        raise SystemExit("unexpected runtype")

    print(perf_counter() - start)


if __name__ == "__main__":
    main()
