from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я помогу вести учёт расходов и доходов для твоего 3D-бизнеса.\n\n"
        "📌 Доступные команды:\n"
        "/add — добавить расход"
    )