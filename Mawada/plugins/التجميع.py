#by Hussein For Mawada-Mawada
# Hussein
# يمنع منعاً باتاً تخمط الملف خلي عندك كرامه ولتسرقة
# Added some f. by Reda

import asyncio
import time
from Mawada import Adyan
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.events import NewMessage
import requests
from telethon.tl.functions.users import GetFullUserRequest
from ..Config import Config
import re
from telethon import events
c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
bot_username5 = '@xnsex21bot'
bot_username6 = '@DamKombot'
bot_username8 = '@Bellllen192BOT'
Mawada = ['yes']
ConsoleJoker = Config.T7KM
its_Reham = False
its_hussein = False
its_reda = False
its_joker = False
#اياثارات الحسين
#by Mustafa doesn't steal codes Please
@Adyan.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع المليار") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username)
        await Adyan.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await Adyan.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Adyan.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"تم الانتهاء من التجميع")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await Adyan.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
@Adyan.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        await Adyan.send_message(bot_username, "/start")
        await event.reply("** ᯽︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")
    
@Adyan.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع مصطفى") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت مصطفى , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username2)
        await Adyan.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(2)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except Exception as er:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**\n{er}")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    #else:
        #await event.edit("يجب الدفع لاستعمال هذا الامر !")
@Adyan.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع العقاب") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username3)
        await Adyan.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await Adyan.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await Adyan.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(3)
            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    #else:
        #await event.edit("يجب الدفع لاستعمال هذا الامر !")
@Adyan.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تجميع المليون") and str(event.sender_id) in ConsoleJoker:
        await event.reply("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username4)
        await Adyan.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(2)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

   # else:
     #   await event.edit("يجب الدفع لاستعمال هذا الامر !")

@Adyan.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await Adyan.get_entity(bot_username)
    await Adyan.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await Adyan.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Adyan.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await Adyan(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Adyan(ImportChatInviteRequest(bott))
            msg2 = await Adyan.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await Adyan.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
        
@Adyan.on(admin_cmd(pattern="(ايقاف التجميع|ايقاف تجميع)"))
async def cancel_collection(event):
    await Adyan.send_message('@EEObot', '/start')
    await event.edit("** ᯽︙ تم الغاء التجميع من بوت المليار **")
    
@Adyan.on(admin_cmd(pattern="(تجميع مصطفى|تجميع جوكر)"))
async def _(event):
    if Mawada[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت مصطفى , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username2)
        await Adyan.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if Mawada[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except Exception as er:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**\n{er}")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

  #  else:
    #    await event.edit("يجب الدفع لاستعمال هذا الامر !")
@Adyan.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if Mawada[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username3)
        await Adyan.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await Adyan.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await Adyan.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if Mawada[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

 #   else:
   #     await event.edit("يجب الدفع لاستعمال هذا الامر !")
@Adyan.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if Mawada[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await Adyan.get_entity(bot_username4)
        await Adyan.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if Mawada[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await Adyan.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Adyan(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Adyan(ImportChatInviteRequest(bott))
                msg2 = await Adyan.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await Adyan.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
        await Adyan.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

#    else:
  #      await event.edit("يجب الدفع لاستعمال هذا الامر !")
@Adyan.on(admin_cmd(pattern="(تجميع العرب|تجميع عرب)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت العرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await Adyan.get_entity(bot_username5)
    await Adyan.send_message(bot_username5, '/start')
    await asyncio.sleep(4)
    msg0 = await Adyan.get_messages(bot_username5, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Adyan.get_messages(bot_username5, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await Adyan(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Adyan(ImportChatInviteRequest(bott))
            msg2 = await Adyan.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await Adyan.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
@Adyan.on(admin_cmd(pattern="تجميع دعمكم"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await Adyan.get_entity(bot_username6)
    await Adyan.send_message('@DamKombot', '/start')
    await asyncio.sleep(4)
    msg0 = await Adyan.get_messages(bot_username6, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await Adyan.get_messages(bot_username6, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message  # الكود تمت كتابتهُ من قبل سورس مصطفى 
        if "اشترك فالقناة @" in msg_text:
            Mustafa_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await Adyan.get_entity(Mustafa_channel)
                if entity:
                    await Adyan(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await Adyan.get_messages(bot_username6, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {chs}")
            except:
                await Adyan.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break

    await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")

@Adyan.on(admin_cmd(pattern="(تجميع عراق|تجميع العراق)"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت العراق , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await Adyan.get_entity(bot_username8)
    await Adyan.send_message(bot_username8, '/start')
    await asyncio.sleep(4)
    msg0 = await Adyan.get_messages(bot_username8, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Adyan.get_messages(bot_username8, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Adyan(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await Adyan(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Adyan(ImportChatInviteRequest(bott))
            msg2 = await Adyan.get_messages(bot_username8, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await Adyan.get_messages(bot_username8, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await Adyan.send_message(event.chat_id, "تم الانتهاء من التجميع")
    
@Adyan.ar_cmd(pattern="راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_hussein
    await event.delete()
    if not its_hussein:
        its_hussein = True
        if event.is_group:
            await send_reham(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def send_reham(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global its_hussein
    if its_hussein:
        await send_reham(event)  
@Adyan.ar_cmd(pattern="ايقاف راتب وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_hussein
    its_hussein = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")
@Adyan.ar_cmd(pattern="بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_joker
    await event.delete()
    if not its_joker:
        its_joker = True
        if event.is_group:
            await send_Mustafa(event)
        else:
            await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_Mustafa(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global its_joker
    if its_joker:
        await send_Mustafa(event)  
@Adyan.ar_cmd(pattern="ايقاف بخشيش وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_joker
    its_joker = False
    await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✓ **")
@Adyan.ar_cmd(pattern="سرقة وعد(?:\s|$)([\s\S]*)")
async def hussein(event):
    global its_reda
    await event.delete()
    if not its_reda:
        its_reda = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await send_message(event, message)
            else:
                await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")

async def send_message(event, message):
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global its_reda
    if its_reda:
        await send_message(event, message)

@Adyan.ar_cmd(pattern="ايقاف سرقة وعد(?:\s|$)([\s\S]*)")
async def Reda(event):
    global its_reda
    its_reda = False
    await event.edit("** ᯽︙ تم ايقاف السرقة بنجاح ✓ **")
client = Adyan

@Adyan.ar_cmd(pattern="استثمار وعد")
async def w3d_joker(event):
    await event.delete()
    global its_Reham
    its_Reham = True
    while its_Reham:
        if event.is_group:
            await event.client.send_message(event.chat_id, "فلوسي")
            await asyncio.sleep(3)
            Mustafa = await event.client.get_messages(event.chat_id, limit=1)
            Mustafa = Mustafa[0].message
            Mustafa = ("".join(Mustafa.split(maxsplit=2)[2:])).split(" ", 2)
            Adyan = Mustafa[0]
            if Adyan.isdigit() and int(Adyan) > 500000000:
                await event.client.send_message(event.chat_id,f"استثمار {Adyan}")
                await asyncio.sleep(5)
                joker = await event.client.get_messages(event.chat_id, limit=1)
                await joker[0].click(text="اي ✅")
            else:
                await event.client.send_message(event.chat_id, f"استثمار {Adyan}")
            await asyncio.sleep(1210)
        
        else:
            await event.edit("** ᯽︙ امر الاستثمار يمكنك استعماله في المجموعات فقط 🖤**")
@Adyan.ar_cmd(pattern="ايقاف استثمار وعد")
async def disable_w3d(event):
    global its_Reham
    its_Reham = False
    await event.edit("**تم تعطيل عملية الاستثمار وعد.**")
