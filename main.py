import asyncio

from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from handlers import router

env = dotenv_values(".env")
bot = Bot(token=env.get("BOT_TOKEN"))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
