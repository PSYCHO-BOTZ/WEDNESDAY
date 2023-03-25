class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {},

ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs, jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴɪᴏʏ</b>"""
    
    HELP_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""


# ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """<b>✯ ᴍʏ ɴᴀᴍᴇ: {}
× ᴍʏ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/zeeroworld>ᴍɪᴋᴇʏ sᴀᴍᴀ</a>
× ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ
× ʟᴀɴɢᴜᴀɢᴇ:  ᴘʏᴛʜᴏɴ 𝟹
× ᴅᴀᴛᴀ ʙᴀsᴇ: ᴍᴀɴɢᴏ ᴅʙ
× ʙᴏᴛ sᴇʀᴠᴇʀ: ʜᴇʀᴏᴋᴜ
× ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v2.0.1 [ ʙᴇᴛᴀ ]</b>
× ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <a href=https://t.me/psycho_association>ᴘsʏᴄʜᴏ ɴᴇᴛᴡᴏʀᴋ</a></b>"""

    SOURCE_TXT = """<b>ᴩʜуꜱᴄᴏ ᴀssᴏᴄɪᴀᴛɪᴏɴ</b>

<b>-ᴩʜуꜱᴄᴏ ɪs ᴀɴ ᴀɴɪᴍᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡʜɪᴄʜ ɪs ᴀ sᴇʀᴠɪᴄᴇ ᴘʀᴏᴠɪᴅɪɴɢ ɴᴇᴛᴡᴏʀᴋ ғᴏʀ ᴀɴɪᴍᴇ ʀᴇʟᴀᴛᴇᴅ sᴛᴜғғs ᴀᴄʀᴏss ᴅɪғғᴇʀᴇɴᴛ ᴘʟᴀᴛғᴏʀᴍs. ɪᴛ ɪs ᴀ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴍᴀᴅᴇ ғᴏʀ ʀᴀɪsɪɴɢ ᴜᴘ ᴏғ ᴀɴɪᴍᴇ ᴄᴏɴᴛᴇɴᴛ ɪɴ ɪɴᴅɪᴀ.

- ᴡʜʏ ʏᴏᴜ sʜᴏᴜʟᴅ sᴜᴘᴘᴏʀᴛ ᴩʜуꜱᴄᴏ</b>

<b> -ᴡᴇ ɴᴇᴇᴅ sᴜᴘᴘᴏʀᴛ ᴏғ ᴛʜᴇ ᴀɴɪᴍᴇ ᴠɪᴇᴡᴇʀs ᴛᴏ ᴋᴇᴇᴘ ᴜs ᴍᴏᴛɪᴠᴀᴛᴇᴅ ᴛᴏ ɪɴᴄʀᴇᴀsᴇ ᴏᴜʀ sᴇʀᴠɪᴄᴇ ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ.  ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ᴍᴀᴋᴇs ᴜs ᴘᴜsʜ ᴏᴜʀsᴇʟᴠᴇs ᴀ sᴛᴇᴘ ғᴜʀᴛʜᴇʀ. ᴡᴇ ᴋɴᴏᴡ ᴏᴜʀ ᴅʀᴇᴀᴍ ᴏғ ʙʀɪɴɢɪɴɢ ᴀɴɪᴍᴇ ɪɴ ɪɴᴅɪᴀ ɪs sɪʟʟʏ ʙᴜᴛ ᴡʜᴀᴛ's ᴛʜᴇ ᴘᴏɪɴᴛ ᴏғ ɪᴛ, ɪғ ᴡᴇ ᴄᴀɴ'ᴛ ʙᴇʟɪᴇᴠᴇ ɪɴ ᴏᴜʀsᴇʟᴠᴇs. ᴡᴇ ᴡᴏɴ'ᴛ ɢɪᴠᴇ ᴜᴘ ᴏɴ ᴏᴜʀ ᴅʀᴇᴀᴍ. ʀᴇsᴛ ɪs ᴜᴘᴏɴ ʏᴏᴜ ɢᴜʏs, ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏʀ ɴᴏᴛ.</b>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>-ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴡᴇᴅɴᴇsᴅᴀʏ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ.</b>

<b>ɴᴏᴛᴇ-</b>
<b>𝟷. ᴡᴇᴅɴᴇsᴅᴀʏ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
𝟸. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
𝟹. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀs.</b>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>ᴡᴇᴅɴᴇsᴅᴀʏ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.</b>
<b>ɴᴏᴛᴇ -</b>
<b>𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴡᴇᴅɴᴇsᴅᴀʏ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ</b>

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs-</b>
<code>[Button Text](buttonurl:https://t.me/Example...)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs-</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>ɴᴏᴛᴇ-</b>
<b>𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
𝟹. ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs.

 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.</b>
<b>★ /set_template - sᴇᴛ ᴄᴜsᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ.</b>
<b>★ /get_template - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ.</b>
<b>★ /autofilter on - ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘs.</b>
<b>★ /autofilter off - ᴅɪsᴀʙʟᴇ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘs.</b>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ</b>

<i>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜsɪᴄ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ᴡɪᴛʜ sᴜᴘᴇʀ ғᴀsᴛ sᴘᴇᴇᴅ. ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs../</i>

<b>ᴄᴏᴍᴍᴀɴᴅs</b>

⏭️ /song sᴏɴɢ ɴᴀᴍᴇ

<b>ᴡᴏʀᴋs ʙᴏᴛʜ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ</b>
module added by - @xenxd"""

    VIDEO_TXT ="""ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.
• ᴜsᴀɢᴇ
ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
ʜᴏᴡ ᴛᴏ ᴜsᴇ
• ᴛʏᴘᴇ /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)

• ᴇxᴀᴍᴘʟᴇ:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

⚠️ This service has been stopped"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    DEPLOY_TXT= """ɪғ  ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇ ɪɴ ᴛʜᴇ ʀᴇᴘᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.

• /ping - <b>To get your ping.</b>

<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
 
    STICKER_TXT = """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ғɪɴᴅ ᴀɴʏ sᴛɪᴄᴋᴇʀs ɪᴅ.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ ʜᴏᴡ ᴛᴏ ᴜsᴇ
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """⚙️ ᴜsᴀɢᴇ

ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ғᴏɴᴛ sᴛʏʟᴇ

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @psycho_association"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

•/whois :-give a user full details 📑"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b> ɪᴜsᴛ sᴏᴍᴇ ᴋɪɴᴅ ᴏғ ғᴜɴ ᴛʜɪɴɢ's </b>
 
𝟣. /dice - ʀᴏʟᴇ ᴛʜᴇ ᴅɪᴄᴇ
𝟤. /Throw 𝗈𝗋 /Dart -  ᴛᴏ ᴍᴀᴋᴇ ᴅᴀʀᴛ
3. /Runs - sᴏᴍᴇ ʀᴀɴᴅᴏᴍ ᴅɪᴀʟᴏɢᴜᴇs
4. /Goal or /Shoot - ᴛᴏ ᴍᴀᴋᴇ ᴀ ɢᴏᴀʟ ᴏʀ sʜᴏᴏᴛ
5. /luck or /cownd - sᴘɪɴ ᴀɴᴅ ᴛʀʏ ʏᴏᴜʀ ʟᴜᴄᴋ"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
• /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""
    
    STATUS_TXT = """<b>× ᴛᴏᴛᴀʟ ғɪʟᴇs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴄʜᴀᴛs - <code>{}</code>
× ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{}</code> ᴍʙ
× ғʀᴇᴇ sᴛᴏʀᴀɢᴇ - <code>{}</code> ᴍʙ</b>"""

    CARB_TXT = """<b>Help</b> : ᴄᴀʀʙᴏɴ
ᴄᴀʀʙᴏɴ ɪs ᴀ ғᴇᴜᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀs sʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴘ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛs.
ғᴏʀ ᴜsɪɴɢ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ɪᴜsᴛ sᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ɪᴛ ᴡɪᴛʜ /carbon ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
@moviesX7_bot
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
@moviesX7_bot
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """
<b>
ʜᴇʟʟᴏ {},

ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴɪᴍᴇ ᴡᴇʙsᴇʀɪᴇs , ɪᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴɪᴏʏ 
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>🔖 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

‣ ɢᴇɴʀᴇs : {genres}
‣ ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> /10 
‣ ʏᴇᴀʀ : {release_date}
‣ ʟᴀɴɢᴜᴀɢᴇ : {languages}
‣ ᴄᴏᴜɴᴛʀʏ : {countries}

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """<b>📂ɴᴀᴍᴇ : {file_name}

» @Team_netflix"

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ʏᴇᴛ  ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇꜱ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ. 
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 

➠ ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ 
➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ 
➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ
➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ 
➠ ᴇxᴀᴍᴘʟᴇ : ᴋᴀɴᴛᴀʀᴀ 2022 

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ' : ( ! , . / )"""

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    REPRT_MSG = """ Reported To Admin"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
