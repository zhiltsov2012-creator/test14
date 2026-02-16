from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
import os

from data import ROADMAPS
from utils import generate_pdf_report

router = Router()

@router.callback_query(F.data.startswith('road_'))
async def roadmap_chosen(callback: CallbackQuery, state: FSMContext):
    road_key = callback.data.split('_')[1]
    roadmap_text = ROADMAPS.get(road_key, "Маршрут не определён")
    
    data = await state.get_data()
    data['roadmap_text'] = roadmap_text
    
    pdf_path = generate_pdf_report(data)
    
    document = FSInputFile(pdf_path, filename="tech_leader_report.pdf")
    await callback.message.answer_document(
        document,
        caption="✅ Ваш персональный отчёт сгенерирован. Сохраните файл как карту перехода!"
    )
    
    await callback.message.answer(
        "🎖 <b>ПЛАН ПЕРЕХОДА СОСТАВЛЕН</b>\n\n"
        "PDF‑файл содержит все данные: профиль, целевые роли, примеры конвертации, дорожную карту.\n\n"
        "Верьте в себя — вы нужны гражданской технологической индустрии!"
    )
    
    await state.clear()
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    
    await callback.answer()