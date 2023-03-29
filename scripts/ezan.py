#!/bin/python3

#----------------------------------------------------------------------------
# Created By  : github/ysfsvm
# Created Date: 29.03.2023
# license = MIT
#----------------------------------------------------------------------------

try:
    import requests
    from datetime import datetime
    import emoji
    from termcolor import colored
except ImportError:
    print("Programın çalışabilmesi için gerekli bağımlılıklar yüklenmemiş!")
    print("Bağımlılıkları yüklemek için aşağıdaki komutları terminale girin:")
    print("pip install requests")
    print("pip install termcolor")
    print("Gerekirse 'pip install emoji' komutunu da girebilirsiniz.")

city = input("Şehir: ")

# Method 13 = Diyanet İşleri Başkanlığı, Turkey
api_url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=Turkey&method=13"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()['data']
    timings = data['timings']

    # Vakitlerin Türkçe karşılıkları ve emojileri
    vakitler = {
        'Fajr': emoji.emojize(':new_moon: İmsak  '),
        'Sunrise': emoji.emojize(':sunrise: Güneş  '),
        'Dhuhr': emoji.emojize(':sun:  Öğle   ' ),
        'Asr': emoji.emojize(':sunset: İkindi '),
        'Maghrib': emoji.emojize(':bridge_at_night: Akşam  '),
        'Isha': emoji.emojize(':night_with_stars: Yatsı  ')
    }

    # Tablo oluşturmak için hücre genişliklerini hesapla
    max_len = max([len(v) for v in vakitler.values()])
    cell_width = max(max_len, 5) + 2  # 5 karakterden kısa olmamalı

    # Tablo başlığı
    table = f"\n{'-' * (cell_width * 2 - 4)}"
    table += f"\n|{' Vakit':^{cell_width-1}}|{'Saat':^{cell_width-6}}|\n"
    table += f"{'-' * (cell_width * 2 - 4)}\n"

    # Vakitleri tabloya ekle
    for vakit, saate in vakitler.items():
        time_str = datetime.strptime(timings[vakit], '%H:%M').strftime('%H:%M')
        table += f"| {colored(saate, 'yellow'):<{cell_width}} | {colored(time_str, 'green'):^{cell_width}} |\n"
    table += f"{'-' * (cell_width * 2 - 4)}"
    print(table)
    print("| 💀 API:aladhan.com |")
    print("----------------------\n")
else:
    print(colored("\033[31mHata: İstek yapılamadı.\033[0m", 'red'))
