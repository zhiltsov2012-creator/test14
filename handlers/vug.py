from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states import TechLeaderQuest
from data import SITUATIONS
from keyboards import situation_keyboard

router = Router()

@router.callback_query(TechLeaderQuest.vug, F.data.startswith('vug_'))
async def vug_chosen(callback: CallbackQuery, state: FSMContext):
    vug_code = callback.data.split('_')[1]
    await state.update_data(vug=vug_code)
    await state.set_state(TechLeaderQuest.sit1)
    
    sit = SITUATIONS[0]
    await callback.message.edit_text(
        f"<b>{sit['text']}</b>",
        reply_markup=situation_keyboard(1, sit['options'])
    )
    await callback.answer()