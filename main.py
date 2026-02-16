import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers import start, vug, situations, result, roadmap

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(start.router)
    dp.include_router(vug.router)
    dp.include_router(situations.router)
    dp.include_router(result.router)
    dp.include_router(roadmap.router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())