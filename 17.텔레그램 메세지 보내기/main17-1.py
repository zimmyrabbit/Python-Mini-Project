import asyncio
import telegram
from info import info

async def get_telegram_id(delay):
    token = info.telegram_token()
    chat = telegram.Bot(token=token)
    updates = await chat.getUpdates()
    await asyncio.sleep(delay)
    for u in updates:
        print(u.message)

async def main():

    await get_telegram_id(1)

asyncio.run(main())