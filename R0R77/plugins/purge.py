from telethon import events, Button
from JE313P import JE313P
from JE313P.status import *
import time

PR_HELP = """
**✘ئه مه به شه فه رمانه کانی پارکردنه وه یه له تایبه ت**

‣ `پاکردنەوە!`
بە وەڵامدانەوەی نامەیەک بۆ سڕینەوەی نامەکانی خوارەوەی

‣ `سرینه وه!`
وەڵامی نامەیەک بدەرەوە بۆ سڕینەوەی


"""

@JE313P.on(events.NewMessage(pattern=r"^[?!]باکردنه وه"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
         await event.reply("سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "پێویستە لە خوارەوە وەڵامی ئەو نامەیە بدەیتەوە کە دەتەوێت بیسڕیتەوە")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"پاکراوەتەوە لە {time_:0.2f} لە چرکە"
    await event.respond(text, parse_mode='markdown')



@JE313P.on(events.NewMessage(pattern="^[!?/]سرینه وه$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
       await event.reply("- سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("پێویستە وەڵامی ئەو نامەیە بدەیتەوە کە دەسڕدرێتەوە")
      return

    await msg.delete()
    await event.delete()

@JE313P.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("گه رانه وه", data="help")]])
