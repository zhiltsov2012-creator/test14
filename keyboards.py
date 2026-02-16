from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import VUG_CHOICES

def vug_keyboard():
    builder = InlineKeyboardBuilder()
    for code, desc in VUG_CHOICES.items():
        builder.button(text=f"{code} – {desc[:30]}...", callback_data=f"vug_{code}")
    builder.adjust(1)
    return builder.as_markup()

def situation_keyboard(sit_num: int, options: dict):
    builder = InlineKeyboardBuilder()
    for key, text in options.items():
        builder.button(text=f"{key}. {text[:40]}...", callback_data=f"sit{sit_num}_{key}")
    builder.adjust(1)
    return builder.as_markup()

def roadmap_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🟢 Госкорпорация", callback_data="road_go_corp")
    builder.button(text="🟡 Интегратор/Пром", callback_data="road_integrator")
    builder.button(text="🔴 Стартап", callback_data="road_startup")
    builder.adjust(1)
    return builder.as_markup()