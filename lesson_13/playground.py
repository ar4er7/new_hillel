# #
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
