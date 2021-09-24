# By < @Godmrunal >
# // @Botz_Official
#dont remove credit else gay

from .. import BotzOfficial
from telethon import events, Button

@BotzOfficial.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("**Hello!**",
                   buttons = [
    [
        Button.url("Updates", url="https://t.me/Botz_Official"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/BotzOfficial_Support"),
    ],
    [Button.inline("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ❔", data="help_back")]
    ])

@BotzOfficial.on(events.callbackquery.CallbackQuery(data="help_back"))
async def ex(event):
    await event.edit("**Here is commands**",
                      buttons=[
                     [Button.inline("        ✘huehue✘        ", data="bsdk")]                     
                     ])

@BotzOfficial.on(events.callbackquery.CallbackQuery(data="bsdk"))
async def ex(event):
    await event.edit("**test message add here anything**",
                     buttons=[
                        [Button.inline("Back!", data="help_back")]
                         ])
