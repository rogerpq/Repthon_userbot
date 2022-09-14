from telethon import events
import random, re
from jepthon.utils import admin_cmd
import asyncio 

@borg.on(admin_cmd("تنصيب السورس"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌁︙**اهـلا بك فـي تنصيب السورس** \n⌁︙رابط التنصيب  - (https://dashboard.heroku.com/new?template=https://github.com/rogerpq/ZQ_LO)[اضغط هنا](⌁︙ يرجى متابعة قناة ريبثون الرسمية لتنصيب السورس - @Repthon)\n⌁︙قناة السورس - @Repthon")
