from f import *
from a import *
from c import *
from e import *
import os

APP_ID = os.environ.get("21159773")
API_HASH = os.environ.get("49ae08543a07335e195756eba2f56e11")
BOT_TOKEN = os.environ.get("6730567676:AAFfMaZCIbPUj2X9T7ZdVWsFtwlwRd3oN14")
DB_URI = os.environ.get("mongodb+srv://aaroha:aaroha@cluster0.6jc4x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DB_URI = os.environ.get("DB_URI")
client = TelegramClient('ShortUrlLink', APP_ID).start(
    bot_token=BOT_TOKEN)

from f import *
start_message = """<b>
Hey There, {}
🔀 I Can Convert Link To ShortLink
💬 Send Me Any Message With Links
🔗 I Will Shorten All Links In It 
🔂 Convert to <a href="https://du-link.in/member/tools/bookmarklet">ShortUrlLink</a> & <a href="https://playdisk.xyz/member/tools/bookmarklet">PlayDisk</a>

©️Powered By @A2z_tech
</b>"""
start_button = [[Button.url("Join Channel ♥️", "t.me/A2z_tech"), Button.inline("About Bot 🤖", "abt")],
                [Button.inline("Connect To Shortner 🔗", 'api')]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [[Button.url("Shorturllink.in", "https://du-link.in/member/tools/bookmarklet")],
              [Button.url("Playdisk.xyz", "https://playdisk.xyz/member/tools/bookmarklet")]]

about_text = """<b>



🤖 Name :  Shorurllink Link Convertor

🔠 Language : Python3
📚 Library     : Telethon
🧑🏻‍💻 Developer : @Ziko_0000

©️Powered By @A2z_tech
</b>"""
