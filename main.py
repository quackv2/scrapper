from defs import getUrl, getcards, phone
from flask import Flask
import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
import random_address
from random_address import real_random_address
import names
from datetime import datetime
import time
import random
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

API_ID = 23444072
API_HASH = '1c5c0cf6dcd43ab5b506a0ff1aa9e48b'
SEND_ID = -1976981266
client = TelegramClient('session', API_ID, API_HASH)
ccs = []
chats = [
    '@LalaScrapperPublic',
    '@AstralScrapper',
    '@VegetaScrap',
    '@JLScrapper',
    '@BINEROS_CCS2',
    '@ozarkscrapper',
    '@ChatA2Assiad',
    '@kurumichat',
    '@techzillacheckerchat',
    '@oficialscorpionsgrupo',
    '@PublicExp',
    '@JohnnySinsChat',
    '@NfPrBroScraper',
    '@VenexChk',
    '@hcccdrops',
    '@ScrapperLost',
    '@CcsRoyals',
    '@RemChatChk',
    '@TeamBlckCard',
    '@astachkccs',
    '@ScrapeLive',
    '@leonbinerss',
    '@SexyDrops',
    '@kurumichks',
    '@binners_LA',
    '@CHECKEREstefany_bot',
    '@scrapper_ddrbins',
    '@valeryscrapp',
    '@ChatPFL',
    '@dSnowChat',
    '@KiraAccountsGrupo',
    '@onyxlivespublic',
    '@botsakuraa'

]
with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on(events.NewMessage(chats=chats, func=lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://lookup.binlist.net/{cc[:6]}')
    if not bin:
        return
    bin_json =  bin.json()
    addr = real_random_address()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}|{names.get_full_name()}|{addr['address1']}|{addr['city']}|{addr['state']}|{addr['postalCode']}|{phone()}|dob: {datetime.strftime(datetime(random.randint(1960, 2005), random.randint(1, 12),random.randint(1, 28), ), '%Y-%m-%d')}|United States Of America"

    print(f'{cc}|{mes}|{ano}|{cvv} - SCRAPPED SUCCESS ')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
    foto_aurora = random.choice(["aurora1.jpg", "aurora2.jpg", "aurora3.jpg", "aurora4.jpg", "aurora5.jpg"])
    await client.send_message(
        PeerChannel(SEND_ID),
        f"""
.　 *　.　　𝐃𝐘𝐂𝐁𝐍 𝐒𝐜𝐫𝐚𝐩𝐩𝐞𝐫　　. 　 ° 　. ● ° .


𝐂𝐂 : ```{cc}|{mes}|{ano}|{cvv}```

- - - - - - - - - - - - - - - - - - - - - - - - 
⌜☾⌟ 𝐁𝐢𝐧 :  [ ```{cc[:6]}``` ]
⌜☾⌟ 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 » : {bin_json['scheme']} - {bin_json['type']} - {bin_json['brand']}
⌜☾⌟ 𝗕𝗮𝗻𝗸 » : {bin_json['bank']['name']}
⌜☾⌟ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » : {bin_json['country']['name']} - {bin_json['country']['emoji']}
- - - - - - - - - - - - - - - - - - - - - - - - 

⌜☂⌟ ᴇxᴛʀᴀ: ```{extra}xxxx|{mes}|{ano}|rnd```

ʕ　·ᴥ·ʔ 𝘿𝙚𝙫 : [ @ReyAustin ]

    ━━━━━━━━━━[⭐️]━━━━━━━━━━
    𝙳𝚈𝙲𝙱𝙽 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 | 𝙑𝙋𝙎 11.4
    https://t.me/+AS6e8eQdKshkMjJh
    ━━━━━━━━━━[⭐️]━━━━━━━━━━

★　　★°★ . *. °☆ . ● . ★　☆　★ ° ☆ ¸. ¸★
""")


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'.lives')))
async def my_event_handler(m):
    # emt = await client.get_entity(1582775844)
    # print(telethon.utils.get_input_channel(emt))
    # print(telethon.utils.resolve_id(emt))
    await m.reply(file='cards.txt')
    time.sleep(3)


client.start()
client.run_until_disconnected()
