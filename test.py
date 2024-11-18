import asyncio
import time


async def fetch_data_1():
    print("Начинаю загрузку данных...")
    await asyncio.sleep(2)  # Имитация долгого запроса
    print("Данные загружены.")


async def fetch_data_2():
    print("Начинаю загрузку данных...")
    await asyncio.sleep(2)  # Имитация долгого запроса
    print("Данные загружены.")


async def main():
    print("Запускаю функции...")
    start_time = time.time()
    await asyncio.gather(fetch_data_1(), fetch_data_2())
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} сек")

# Запуск асинхронной программы
asyncio.run(main())
