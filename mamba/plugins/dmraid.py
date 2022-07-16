from pyrogram import filters, Client
from pyrogram.types import *
import asyncio
from random import choice
from helpers.data import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      hero = await e.reply_text("⚡ ᴜsᴀɢᴇ:\n !dmraid 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")
      Mamba = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Mamba) == 2:
          ok = await xspam.get_users(Mamba[1])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ᴍᴀᴍʙᴀ`"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`"
                await e.reply_text(text)
          else:
              counts = int(Mamba[0])
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.002)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"`ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ᴍᴀᴍʙᴀ`"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`"
                await e.reply_text(text)
          else:
              counts = int(Mamba[0])
              await e.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.002)

