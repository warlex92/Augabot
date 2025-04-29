from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="💰 Стоимость ОСАГО")],
        [KeyboardButton(text="📝 Необходимые документы")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)
