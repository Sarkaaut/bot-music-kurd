from SARKAUT import SARKAUT, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
 👋┇بەخێر بێیت ئازیزم ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
‣ **من بۆتێکی سادەم بۆ پاراستنی گروپەکەت و پەخشکردنی کلیپی دەنگی لە پەیوەندییەکدا**.
‣ **دەتوانم کلیپی دەنگی لە کاتی پەیوەندیدا لێبدەم**.
‣ **دەتوانم هەر بەکارهێنەرێک بلۆک بکەم و بێدەنگ بکەم**.
‣ **باشترین بۆت لە ڕووی تایبەتمەندییەوە**.
‣ **لەسەر بنەمای کتێبخانەی Telethon دروستکراوە بۆیە بۆتەکە خێرایە**!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
"""

@SARKAUT.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ بۆ ئادم کلیک لێرە بکە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("خاوه ن بۆت", "https://t.me/SARKAUT")],
        [Button.url("پشتگیری", f"https://t.me/{Config.SUPPORT}"), Button.url("که ناڵ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("فه رمانه کان", data="help")]])
       return

    if event.is_group:
       await event.reply("**- من بە سەرکەوتوویی کار دەکەم**")
       return



@SARKAUT.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ بۆ ئادم کلیک لێرە بکە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("خاوه ن بۆت", "https://t.me/SARKAUT")],
        [Button.url("پشتگتری", f"https://t.me/{Config.SUPPORT}"), Button.url("که ناڵ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("فه رمانه کان", data="help")]])
       return
