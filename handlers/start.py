from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import vug_keyboard
from states import TechLeaderQuest

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "🎖 <b>«Точка технологического перехода»</b>\n\n"
        "Этот квест поможет вам сохранить компетенции технологического лидера "
        "при переходе с военной службы на гражданскую работу.\n\n"
        "Вы пройдёте 5 этапов:\n"
        "1. Выбор военно-учётной группы\n"
        "2. Определение вашего архетипа лидера\n"
        "3. Подбор родственной профессии (уровень Tech Lead)\n"
        "4. Конвертация достижений\n"
        "5. Персональная дорожная карта\n\n"
        "Готовы? Нажмите /start_q"
    )

@router.message(Command('start_q'))
async def start_quest(message: Message, state: FSMContext):
    await state.set_state(TechLeaderQuest.vug)
    await message.answer(
        "Выберите вашу военно-учётную группу:",
        reply_markup=vug_keyboard()
    )