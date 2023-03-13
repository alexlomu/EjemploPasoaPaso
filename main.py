import asyncio 
import aiohttp
import random
import os 
import time

async def descarga(session, url):
    try:
        inicio = time.monotonic()
        async with session.get(url) as response:
            content = await response.read()
            filename = f"{url.split('/')[-1]}.png"
            filepath = os.path.join("imagenes", filename)
            with open(filepath, "wb") as file:
                file.write(content)
                final = time.monotonic()
                print(f"{filename} downloaded in {final - inicio:.2f} seconds")
    except Exception as e:
        print(f"HA OCURRIDO UN ERROR {url}: {e}")

async def seleccion(num_imagenes):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_imagenes):
            url = f"https://picsum.photos/{random.randint(200, 500)}/{random.randint(200, 500)}"
            task = asyncio.ensure_future(descarga(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_imagenes = 10
    if not os.path.exists("imagenes"):
        os.mkdir("imagenes")
    asyncio.run(seleccion(num_imagenes))