from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states import TechLeaderQuest
from data import SITUATIONS
from keyboards import situation_keyboard

router = Router()

@router.callback_query(TechLeaderQuest.sit1, F.data.startswith('sit1_'))
async def sit1_answered(callback: CallbackQuery, state: FSMContext):
    answer = callback.data.split('_')[1]
    await state.update_data(sit1=answer)
    await state.set_state(TechLeaderQuest.sit2)
    
    sit = SITUATIONS[1]
    await callback.message.edit_text(
        f"<b>{sit['text']}</b>",
        reply_markup=situation_keyboard(2, sit['options'])
    )
    await callback.answer()

@router.callback_query(TechLeaderQuest.sit2, F.data.startswith('sit2_'))
async def sit2_answered(callback: CallbackQuery, state: FSMContext):
    answer = callback.data.split('_')[1]
    await state.update_data(sit2=answer)
    await state.set_state(TechLeaderQuest.sit3)
    
    sit = SITUATIONS[2]
    await callback.message.edit_text(
        f"<b>{sit['text']}</b>",
        reply_markup=situation_keyboard(3, sit['options'])
    )
    await callback.answer()

@router.callback_query(TechLeaderQuest.sit3, F.data.startswith('sit3_'))
async def sit3_answered(callback: CallbackQuery, state: FSMContext):
    answer = callback.data.split('_')[1]
    await state.update_data(sit3=answer)
    
    from handlers.result import show_results
    await show_results(callback.message, state)
    await callback.answer()