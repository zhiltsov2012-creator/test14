from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data import PROFESSIONS_TABLE, CONVERSION_EXAMPLES
from keyboards import roadmap_keyboard

async def show_results(message: Message, state: FSMContext):
    data = await state.get_data()
    vug = data.get('vug')
    answers = [data.get('sit1'), data.get('sit2'), data.get('sit3')]
    
    count_a = answers.count('А')
    count_b = answers.count('Б')
    count_c = answers.count('В')
    
    if count_a >= count_b and count_a >= count_c:
        archetype = 'А'
        archetype_name = 'Командир'
    elif count_b >= count_a and count_b >= count_c:
        archetype = 'Б'
        archetype_name = 'Технарь'
    else:
        archetype = 'В'
        archetype_name = 'Аналитик'
    
    professions = PROFESSIONS_TABLE.get((vug, archetype), 'Подходящие позиции не найдены.')
    
    await state.update_data(archetype=archetype, archetype_name=archetype_name, professions=professions)
    
    text = (
        f"✅ <b>Ваш профиль технологического лидера</b>\n\n"
        f"• Военно-учётная группа: <b>{vug}</b>\n"
        f"• Архетип: <b>{archetype_name}</b>\n\n"
        f"🎯 <b>Рекомендуемые позиции (уровень Tech Lead / Head):</b>\n{professions}\n\n"
        f"📌 <b>Примеры конвертации достижений:</b>\n"
    )
    for ex in CONVERSION_EXAMPLES:
        text += f"{ex}\n"
    
    text += "\n\nВыберите ваш предпочтительный маршрут входа на гражданку:"
    
    await message.edit_text(text, reply_markup=roadmap_keyboard())