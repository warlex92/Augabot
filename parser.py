import aiohttp

# Получаем курс евро к рублю с сайта ЦБ РФ
async def get_eur_to_rub_rate():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json(content_type=None)  # <--- добавил content_type=None чтобы избежать ошибки!
                eur_rate = data['Valute']['EUR']['Value']  # Цена 1 евро в рублях
                return eur_rate
            else:
                raise Exception(f"Ошибка получения курса валют: {response.status}")

# Тарифы в рублях
TARIFFS_RUB = {
    "<36.8 кВт / 50 лс": [1241.46, 2280.79, 3041.05, 3801.31, 5321.84, 7602.63],
    "36.8-51.5 кВт / 50-70 лс": [2069.10, 3801.31, 5068.42, 6335.52, 8869.73, 12671.04],
    "51.5-73,6 кВт / 70-100 лс": [2276.01, 4181.44, 5575.26, 6969.07, 9756.70, 13938.15],
    "73,6-88,3 кВт / 100-120 лс": [2482.92, 4561.58, 6082.10, 7602.63, 10643.68, 15205.25],
    "88,3-110,3 кВт / 120-150 лс": [2896.74, 5321.84, 7095.78, 8869.73, 12417.62, 17739.46],
    "> 110.3 кВт / 150 лс": [3310.56, 6082.10, 8109.47, 10136.84, 14191.57, 20273.67],
    "Грузовой автомобиль Кат. С": [3312.56, 4968.83, 6625.11, 8281.39, 11593.95, 16562.78]
}

# Переводим тарифы в евро и готовим текст
async def get_osago_prices():
    try:
        eur_rate = await get_eur_to_rub_rate()
        prices_text = "💰 Актуальные тарифы ОСАГО (в евро):\n\n"
        for power, rub_prices in TARIFFS_RUB.items():
            prices_text += f"▪️ Мощность двигателя: **{power}**\n"
            periods = ["15 дней", "1 месяц", "2 месяца", "3 месяца", "6 месяцев", "12 месяцев"]
            
            for period, rub_price in zip(periods, rub_prices):
                euro_price = round(rub_price / eur_rate)  # округляем до целого
                prices_text += f"📅 {period} — **{euro_price} €**\n"  # без .2f
            
            prices_text += "\n"
        
        prices_text += "✅ Курс валют обновляется автоматически.\n"
        prices_text += "Подробнее: [Перейти на сайт](https://augapost.com/ru/osago)"

        return prices_text
    except Exception as e:
        return f"Ошибка при получении данных: {str(e)}"
