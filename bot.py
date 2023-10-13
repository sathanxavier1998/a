import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "6620972"))
API_HASH = environ.get("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
BOT_TOKEN = environ.get("BOT_TOKEN", "5557012576:AAFzIKDUqFbtuaVF5O64ebSo1X4iNLZT97Y")
SESSION = environ.get("SESSION", "BQHIlWYAvFg2nM-bese1DtnUHo4_2WP6vre4GO98bbNZIG7rxpNfAh2ropIXwDVNXL_x0-Sxh9-IYqHoNmDqLsdJL92OcgeFeoPeIO4viMFI0UyHnCViNfRIoLWQc6-77SE02CPEo1GQKgdAxqOmxgwhdde9sYYLKeLoVbslBKODSSW-jVCrVQV2Y5e86qUg_wem7I9DARhKvYRZe0-DLoBGwYXcmCHUH08f-DCU8zsdU9p3lyU5VdRyIoYM0syTNAiNKphzrrPd8NyucaaXMLbzt0bwgP-BlvFHeFMSxHOVBOE-k9DeKSc5aQ97pejKgoaW5LY7ocKmSO6egS1RUEOpD0qn1QAAAAFodbDbAA")
TIME = int(environ.get("TIME", "3000"))
GROUPS = []
for grp in environ.get("GROUPS", "-1001570401050").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS", "1745047302" "6047510747").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a private bot of @cinema_villa_grp to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
