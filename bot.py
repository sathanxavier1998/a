import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "6620972"))
API_HASH = environ.get("API_HASH", "3f6835286b03e000ab6d71b37cc35b92")
BOT_TOKEN = environ.get("BOT_TOKEN", "5557012576:AAFzIKDUqFbtuaVF5O64ebSo1X4iNLZT97Y")
SESSION = environ.get("SESSION", "BQHIlWYAHV6c2KPKuP8QlalgdncIcCYP9nFdhD8ZuIgGWPcEbSHpYlvu41PaWj2xaUljcvrusnzNthCxX0IcvMG0ZpynSwROD2cKybk0h99pcQdTCRarNYMPeYkUYcC_zaNRVdSS_WiTOV4ayeIU2RvNDKfhWeVYKF_1CQPAO40YE00otz_Z_aTPWZuMfWZhpvz8jn6Mj8oigb49sRwhTSzKo23cJ49CyirjnWi-sSo5NMg4vPtKBnbW5rrCi-JRf-Iuz3yIyMn1LIC1MCVlcDD5_A7JkTuh7HwCuzHL04SEh5DknVx4t9q_tmvZNck3ale1hQNUyQpy6zedsnsBjK_hbOYPYQAAAAFodbDbAA")
TIME = int(environ.get("TIME", "3000"))
GROUPS = [-1001570401050]
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = [1745047302 6047510747]
for usr in environ.get("ADMINS").split():
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
