import asyncio
import itertools as it
import os
import random
import time

##
# # async def main():
# #     print('hello')
# #     await asyncio.sleep(1)
# #     print('world')
# #
# # asyncio.run(main())


# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())


# async def nested():
#     return 42
#
# async def main():
#     # print(await(nested()))
#     task = asyncio.create_task(nested())
#     # task.cancel()
#     try:
#         await task
#         print("successfully finished")
#     except asyncio.CancelledError:
#         print(f"task is cancelled before")
#
# asyncio.run(main())


# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(2)
#     print("Task 1 completed")
#
# async def main():
#     # Ждем завершения task1 перед продолжением
#     print("main started")
#     await task1()
#     print("Task 1 завершена, продолжаем выполнение main")
#
# asyncio.run(main())


# async def task1():
#     await asyncio.sleep(5)
#     print("Task 1 done")
#
# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 done")
#
# async def main():
#     # Запуск task1 параллельно с остальным кодом
#     task = asyncio.create_task(task1())
#     print("Task 1 запущена параллельно")
#     # Немедленно переходим к task2
#     await task2()  # Ждем завершения task2 перед продолжением
#     print("Task 2 завершена")
#     await task  # Теперь ждем завершения task1
#
# asyncio.run(main())

# pep 0380
# def subgen():
#     yield 1
#     yield 2
#     return "Result from subgen"
#
# def main_gen():
#     result = yield from subgen()
#     print("Subgen returned:", result)
#     yield 3
#
# for item in main_gen():
#     print(item)

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"executed in {elapsed:0.2f} seconds.")


# ANSI colors
# c = (
#     "\033[0m",   # End of color
#     "\033[36m",  # Cyan
#     "\033[91m",  # Red
#     "\033[35m",  # Magenta
# )
#
# async def makerandom(idx: int, threshold: int = 6) -> int:
#     print(c[idx + 1] + f"Initiated makerandom({idx}).")
#     i = random.randint(0, 10)
#     while i <= threshold:
#         print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
#         await asyncio.sleep(idx + 1)
#         i = random.randint(0, 10)
#     print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
#     return i
#
# async def main():
#     res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
#     return res
#
# if __name__ == "__main__":
#     random.seed(444)
#     r1, r2, r3 = asyncio.run(main())
#     print()
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}")


# async def part1(n: int) -> str:
#     i = random.randint(0, 10)
#     print(f"part1({n}) sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-1"
#     print(f"Returning part1({n}) == {result}.")
#     return result
#
# async def part2(n: int, arg: str) -> str:
#     i = random.randint(0, 10)
#     print(f"part2{n, arg} sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-2 derived from {arg}"
#     print(f"Returning part2{n, arg} == {result}.")
#     return result
#
# async def chain(n: int) -> None:
#     start = time.perf_counter()
#     p1 = await part1(n)
#     p2 = await part2(n, p1)
#     end = time.perf_counter() - start
#     print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")
#
# async def main(*args):
#     await asyncio.gather(*(chain(n) for n in args))
#
# if __name__ == "__main__":
#     import sys
#     random.seed(444)
#     args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
#     start = time.perf_counter()
#     asyncio.run(main(*args))
#     end = time.perf_counter() - start
#     print(f"Program finished in {end:0.2f} seconds.")



async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>" f" in {now-t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse

    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
