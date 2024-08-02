#ربي اشرح لي صدري
#تمت كتابة الكود من قبل السيد حسين @rre3l
#فريق مصطفى @rre3l
import asyncio
from telethon import events
from Mawada import Adyan
hussein_enabled = False
Mustafa_enabled = False
JOKER_ID = {}

@Adyan.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global Mustafa_enabled, JOKER_ID
    sender_id = event.sender_id
    if Mustafa_enabled and sender_id in JOKER_ID:
        joker_time = JOKER_ID[sender_id]
        if joker_time > 0:
            await asyncio.sleep(joker_time)
        await event.mark_read()

@Adyan.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر تعطيل$'))
async def Hussein(event):
    global Mustafa_enabled
    Mustafa_enabled = False
    await event.edit('**᯽︙ تم تعطيل امر التكبر بنجاح ✅**')

@Adyan.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر (\d+) (\d+)$'))
async def Hussein(event):
    global Mustafa_enabled, JOKER_ID
    joker_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    JOKER_ID[user_id] = joker_time
    Mustafa_enabled = True
    await event.edit(f'**᯽︙ تم تفعيل امر التكبر بنجاح مع  {joker_time} ثانية للمستخدم {user_id}**')

@Adyan.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر تعطيل$'))
async def Hussein(event):
    global hussein_enabled
    hussein_enabled = False
    await event.edit('**᯽︙ تم تعطيل امر التكبر على الجميع بنجاح ✅**')
    
@Adyan.on(admin_cmd(pattern=f"مود التكبر (\d+)"))
async def Hussein(event):
    global hussein_enabled, hussein_time
    hussein_time = int(event.pattern_match.group(1))
    hussein_enabled = True
    await event.edit(f'**᯽︙ تم تفعيل امر التكبر بنجاح مع  {hussein_time} ثانية**')

@Adyan.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def Hussein(event):
    global hussein_enabled, hussein_time
    if hussein_enabled:
        await asyncio.sleep(hussein_time)
        await event.mark_read()
