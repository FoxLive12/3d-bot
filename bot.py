import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db.database import init_db
from handlers.purchases import router as purchase_router

async def main():
    await init_db()
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(purchase_router)
    
    print("Бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main())