import random
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint as print
from threading import Thread
from time import perf_counter

import requests
from mypy.moduleinspect import Queue

POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2/berry"


def fetch_pokemons(_id: int, queue_: Queue = None) -> dict:
    response: requests.Response = requests.get(url=f"{POKEAPI_BASE_URL}/{_id}")
    if response.status_code != 200:
        print(f"Error: {response.status_code} | {response.text}")
        result = {}
    else:
        result = response.json()
        if queue_:
            queue_.put(result)
    return result


def main_sync(pokemons_number: int):
    results: list[dict] = []
    for _ in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        pokemon = fetch_pokemons(_id=random_id)
        results.append(pokemon)

    return results


def main_threads_queue(pokemons_number):
    fetched_queue = Queue()
    results: list[dict] = []
    threads: list[Thread] = []
    for _ in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        threads.append(Thread(target=fetch_pokemons, args=(random_id, fetched_queue)))
    print(f"{len(threads)=}")

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
        results.append(fetched_queue.get())

    print(f"{len(results)=}")


def main_threads_pool(pokemons_number):
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=pokemons_number) as executor:
        futures = []
        for i in range(pokemons_number):
            futures.append(executor.submit(fetch_pokemons, random.randint(1, 50)))
        print(f"{len(futures)=}")

        for future in as_completed(futures):
            results.append(future.result())

    print(f"{len(results)=}")


def main():
    """Execute qthreads to run threads fetching as queue"""
    """Execute pthreads to run threads fetching as pool executor"""
    try:
        runtype: str = sys.argv[1]
        pokemons_number: int = int(sys.argv[2])
    except IndexError:
        print("please enter the number of pokemons to be fetched")
    except ValueError:
        print("only integers allowed")

    if runtype == "sync":
        main_sync(pokemons_number)
    elif runtype == "qthreads":
        main_threads_queue(pokemons_number)
    elif runtype == "pthreads":
        main_threads_pool(pokemons_number)

    else:
        raise SystemExit("unexpected runtype")


if __name__ == "__main__":
    start = perf_counter()
    main()
    print(f"{perf_counter() - start}")
