from telethon import events, Button
from SARKAUT import SARKAUT, BOT_USERNAME

btn =[
    [Button.inline("بەڕێوەبەر", data="admin"),],
    [Button.inline("دامەزراندن", data="pins"), Button.inline("پاکردنەوە", data="purges")],
    [Button.inline("کار پی کردن", data="play"), Button.inline("لابراوە کان", data="zombies")],
    [Button.inline("قوفڵ", data="locks"), Button.inline("زیاتر", data="misc")],
    [Button.inline("سەرەکی", data="start")]]

HELP_TEXT = "بەخێربێن بۆ لیستی فەرمانەکانی Telethon سەرچاوە\n\nکلیک لە دوگمەکانی خوارەوە بکە:"


@SARKAUT.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
       await event.reply("بۆ بینینی فرمانەکان کلیک لە خوارەوە بکە", buttons=[
       [Button.url("لێرەدا فشار بدە", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@SARKAUT.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@SARKAUT.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
