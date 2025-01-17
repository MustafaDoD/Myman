import asyncio
import time

import aiohttp
from telethon.errors import ChatAdminRequiredError as no_admin
from telethon.tl.functions.messages import ExportChatInviteRequest

from Adyan.jana.resources.strings import *
from Mawada import Adyan
from Mawada.utils import admin_cmd

from ..core.managers import edit_or_reply
from ..core.managers import edit_or_reply as eod
from ..helpers import get_user_from_event
from . import *


@Adyan.on(admin_cmd(pattern="كتابة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع الكتابة الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@Adyan.on(admin_cmd(pattern="صوتية(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الصوتية الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@Adyan.on(admin_cmd(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@Adyan.on(admin_cmd(pattern="لعبة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@Adyan.on(admin_cmd(pattern="الرابط$"))
async def _(e):
    rr = await edit_or_reply(e, "**يتم جلب الرابط انتظر **")
    try:
        r = await e.client(
            ExportChatInviteRequest(e.chat_id),
        )
    except no_admin:
        return await eod(rr, "عذرا انت لست مشرف في هذه الدردشة", time=10)
    await eod(rr, f"- رابط الدردشة\n {r.link}")


@Adyan.on(admin_cmd(pattern="للكل تاك$"))
async def listall(Mawada):
    if Mawada.fwd_from:
        return
    mentions = "- هذه هي قائمة جميع الاعضاء هنا: "
    chat = await bot.get_input_chat()
    async for x in borg.iter_participants(chat, 2000):
        mentions += f" \n[{x.first_name}](tg://user?id={x.id})"
    await Mawada.reply(mentions)
    await Mawada.delete()

R = (
    "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈▏\n"
)


@Adyan.on(admin_cmd(pattern=r"سبونج"))
async def kerz(kerz):
    await kerz.edit(R)

M = (
    "╭━┳━╭━╭━╮╮\n"
    "┃┈┈┈┣▅╋▅┫┃\n"
    "┃┈┃┈╰━╰━━━━━━╮\n"
    "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
    "╲┃┈┈┈┈╭━┳━━━━╯\n"
    "╲┣━━━━━━┫\n"
)


@Adyan.on(admin_cmd(pattern=r"كلب"))
async def dog(dog):
    await dog.edit(M)
Z = (
    "┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)


H = (
    " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈\n"
)

A = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈\n"
)

N = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈┈┈┈\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n"
)



@Adyan.on(admin_cmd(pattern=r"ذئب"))
async def fox(fox):
    await fox.edit(H)


@Adyan.on(admin_cmd(pattern=r"فيل"))
async def elephant(elephant):
    await elephant.edit(A)


@Adyan.on(admin_cmd(pattern=r"هومر"))
async def homer(homer):
    await homer.edit(N)


@Adyan.on(admin_cmd(pattern=r"بك"))
async def pig(pig):
    await pig.edit(Z)
