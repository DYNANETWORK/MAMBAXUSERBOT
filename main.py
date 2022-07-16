import asyncio
import importlib
from mamba import ALL_MODULES
from pyrogram import idle
from config import client, client2, client3, client4, client5, client6, client7, client8, client9, client10, bot, call_py, call_py2, call_py3, call_py4, call_py5, call_py6, call_py7, call_py8, call_py9, call_py10
from config import *


msg = """
» __ᴍᴀᴍʙᴀ ᴜsᴇʀʙᴏᴛ sᴜᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ__
» __ᴍᴀᴍʙᴀ ᴠᴇʀsɪᴏɴ__ = 𝟸.𝟶
» __ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ__ = 𝟷.𝟺.𝟷𝟼

"""

async def main():
    if client:
        try:
            await client.start()
            await client.join_chat("MAMBA_X_SUPPORT")
            await client.join_chat("MAMBA_X_NETWORK")
            await client.join_chat("TG_KI_DUNITA")
            await client.join_chat("ABOUT_MAMBA")
            await client.join_chat("MAMBA_BOT_UPDATES")
            await client.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client2:
        try:
            await client2.start()
            await client2.join_chat("MAMBA_X_SUPPORT")
            await client2.join_chat("MAMBA_X_NETWORK")
            await client2.join_chat("TG_KI_DUNIYA")
            await client2.join_chat("ABOUT_MAMBA")
            await client2.join_chat("MAMBA_BOT_UPDATES")
            await client2.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client3:
        try:
            await client3.start()
            await client3.join_chat("MAMBA_X_SUPPORT")
            await client3.join_chat("MAMBA_X_NETWORK")
            await client3.join_chat("TG_KI_DUNIYA")
            await client3.join_chat("ABOUT_MAMBA")
            await client3.join_chat("MAMBA_BOT_UPDATES")
            await client3.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client4:
        try:
            await client4.start()
            await client4.join_chat("MAMBA_X_SUPPORT")
            await client4.join_chat("MAMBA_X_NETWORK")
            await client4.join_chat("TG_KI_DUNIYA")
            await client4.join_chat("ABOUT_MAMBA")
            await client4.join_chat("MAMBA_BOT_UPDATES")
            await client4.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client5:
        try:
            await client5.start()
            await client5.join_chat("MAMBA_X_SUPPORT")
            await client5.join_chat("MAMBA_X_NETWORK")
            await client5.join_chat("TG_KI_DUNIYA")
            await client5.join_chat("ABOUT_MAMBA")
            await client5.join_chat("MAMBA_BOT_UPDATES")
            await client5.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client6:
        try:
            await client6.start()
            await client6.join_chat("MAMBA_X_SUPPORT")
            await client6.join_chat("MAMBA_X_NETWORK")
            await client6.join_chat("TG_KI_DUNIYA")
            await client6.join_chat("ABOUT_MAMBA")
            await client6.join_chat("MAMBA_BOT_UPDATES")
            await client6.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client7:
        try:
            await client7.start()
            await client7.join_chat("MAMBA_X_SUPPORT")
            await client7.join_chat("MAMBA_X_NETWORK")
            await client7.join_chat("TG_KI_DUNIYA")
            await client7.join_chat("ABOUT_MAMBA")
            await client7.join_chat("MAMBA_BOT_UPDATES")
            await client7.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client8:
        try:
            await client8.start()
            await client8.join_chat("MAMBA_X_SUPPORT")
            await client8.join_chat("MAMBA_X_NETWORK")
            await client8.join_chat("TG_KI_DUNIYA")
            await client8.join_chat("ABOUT_MAMBA")
            await client8.join_chat("MAMBA_BOT_UPDATES")
            await client8.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client9:
        try:
            await client9.start()
            await client9.join_chat("MAMBA_X_SUPPORT")
            await client9.join_chat("MAMBA_X_NETWORK")
            await client9.join_chat("TG_KI_DUNIYA")
            await client9.join_chat("ABOUT_MAMBA")
            await client9.join_chat("MAMBA_BOT_UPDATES")
            await client9.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))

    if client10:
        try:
            await client10.start()
            await client10.join_chat("MAMBA_X_SUPPORT")
            await client10.join_chat("MAMBA_X_NETWORK")
            await client10.join_chat("TG_KI_DUNIYA")
            await client10.join_chat("ABOUT_MAMBA")
            await client10.join_chat("MAMBA_BOT_UPDATES")
            await client10.send_message(-1001549452504, text=msg)
        except Exception as e:
            print(str(e))
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("mamba" + all_module)
    if call_py:
        await call_py.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    if call_py9:
        await call_py9.start()
    if call_py10:
        await call_py10.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
