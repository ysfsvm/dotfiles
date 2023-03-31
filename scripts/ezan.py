#!/bin/python3

#----------------------------------------------------------------------------
# Created By  : github/ysfsvm
# Created Date: 29.03.2023
# license = MIT
#----------------------------------------------------------------------------
import sys
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

# Argüman olarak şehir adı verilmiş mi kontrol et
if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("Lütfen şehir adını girin: ")


api_url = f"https://www.sabah.com.tr/json/getpraytimes/{city.lower()}"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()['List'][0]

    vakitler = {
        'Imsak': emoji.emojize(':new_moon: İmsak  '),
        'Gunes': emoji.emojize(':sunrise: Güneş  '),
        'Ogle': emoji.emojize(':sun:  Öğle   ' ),
        'Ikindi': emoji.emojize(':sunset: İkindi '),
        'Aksam': emoji.emojize(':bridge_at_night: Akşam  '),
        'Yatsi': emoji.emojize(':night_with_stars: Yatsı  ')
    }

    max_len = max([len(v) for v in vakitler.values()])
    cell_width = max(max_len, 5) + 2  # 5 karakterden kısa olmamalı

    table = f"\n{'-' * (cell_width * 2 - 4)}"
    table += f"\n|{' Vakit':^{cell_width-1}}|{'Saat':^{cell_width-6}}|\n"
    table += f"{'-' * (cell_width * 2 - 4)}\n"

    for vakit, saate in vakitler.items():
        time_str = datetime.fromtimestamp(int(data[vakit][6:-2])/1000).strftime('%H:%M')
        table += f"| {colored(saate, 'yellow'):<{cell_width}} | {colored(time_str, 'green'):^{cell_width}} |\n"
    table += f"{'-' * (cell_width * 2 - 4)}"
    print(table)
    print("| 💀 API:sabah.com.tr |")
    print("----------------------\n")
else:
    print(colored("\033[31mHata: İstek yapılamadı.\033[0m", 'red'))

