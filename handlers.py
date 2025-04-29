from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_menu
from parser import get_osago_prices

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        '👋 Оформляем страховые полисы ОСАГО Российской Федерации для автомобилей с регистрацией в ЕС (Евросоюз). Оформление происходит на основании агентского соглашения с компанией АО СК "Двадцать первый век". Полис ОСАГО действует только на территории Российской Федерации.\n\nВыберите нужный пункт меню:',
        reply_markup=main_menu
    )

@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer("📞 Телефон: +372 53581535\n📧 Почта: info@augapost.com")

@router.message(F.text == "💰 Стоимость ОСАГО")
async def osago_price(message: Message):
    prices = await get_osago_prices()
    await message.answer(prices, parse_mode="Markdown")

@router.message(F.text == "📝 Необходимые документы")
async def documents(message: Message):
    await message.answer(
        "Для оформления страховки потребуются:\n"
        "📝 Техпаспорт транспортного средства (фотография или скан с 2-х сторон, хорошего качества, без обрезки полей)\n"
        "📝 Паспорт владельца транспортного средства, указанного в техпаспорте (ID-карточка не подойдет)\n"
        "📝 Сообщить период и дату начала страхования (минимально 15 дней)\n"
        "📝 Сообщить контактные данные\n\n"  # <-- здесь добавлен перенос строки
        "Заявку на оформление необходимо отправить на нашу электронную почту: info@augapost.com"
    )