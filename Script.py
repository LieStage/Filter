import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://tnlink.in/ref/KarthikUK')
    START_TXT = environ.get("START_TXT", '''<b>Hello 👋🏻 {} ♥️,\nI'm an Star Movies Tamil's Official Auto Filter Bot (Movie Search Bot) <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a> Maintained by <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>. We are Providing All Languages. 🌍 Languages :- Tamil, Telugu, Hindi, Malayalam, Kannada, English and Extra... Keep me Join to Our Official Channel to Receive 🎥 Movie Updates in <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>. And Also Keep me Join to Our Official Bot Channel to Receive 🤖 Bot Updates in <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a>. Check "😁 About" Button.</b>''')
    HELP_TXT = """<b>Hello 👋🏻 {} ♥️,
I have that Features.
Create One Link This :-
» I will Create For One Bot You. But Paid
» Contact Me <a href=https://t.me/TG_Karthik><b>Karthik</b></a></b>"""
    ABOUT_TXT = """<b><i>🤖 My Name :- <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a>\n
🧑🏻‍💻 Developer :- <a href=https://t.me/TG_Karthik><b>Karthik</b></a>\n
📝 Language :- Python3\n
📚 Framework :- Pyrogram\n
📡 Hosted on :- VPS\n
🎥 Movie Updates :- <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>\n
🤖 Bot Channel :- <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a>\n
🌟 Version :- 4.4</b></i>"""
    SOURCE_TXT = """<b>Create One Like This :-</b>
» I will Create One Bot For You. But Paid<b>
» Contact Me</b> <a href=https://t.me/TG_Karthik><b>Karthik</b></a>"""
    MANUELFILTER_TXT = """<b>Help :-</b> <b>Filters</b>

<b>- Filter is the Feature Were Users Can set Automated Replies for a Particular Keyword and <a href=https://t.me/Star_Moviess_Bot><b>Our Bot</b></a> will Respond Whenever a Keyword is Found the Message</b>

<b>NOTE :-</b>
<b>1. <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a> Should have 👨🏻‍✈️ Admin Privillage.
2. Only 👨🏻‍✈️ Admins can Add Filters in a Chat.
3. Alert Buttons have a Limit of 64 Characters.</b>

<b>Commands and Usage :-</b>
<b>• /filter - Add a Filter in Chat
• /filters - List all the Filters of a Chat
• /gfilter - Add a Global Filter in Chat
• /gfilters - List all the Global Filters of a Chat
• /del - Delete a Specific Filter in Chat 
• /delall - Delete the Whole Filters in a Chat (Chat Owner Only)
• /delg - Delete 🗑️ a Specific Global Filter in Chat 
• /delallg - Delete the Whole Global Filters</b>"""
    BUTTON_TXT = """<b>Help :-</b> <b>Buttons</b>

<b>- <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a> Supports Both URL and Alert Inline Buttons.</b>

<b>NOTE :-</b>
<b>1. Telegram will Not Allows you to Send Buttons Without Any Content, so Content is Mandatory.
2. <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a> supports Buttons With Any Telegram Media/File type.
3. Buttons Should be Properly Parsed as Markdown Format</b>

<b>URL Buttons :-</b>
<code>[Button Text](buttonurl:https://t.me/Star_Moviess_Tamil)</code>

<b>Alert Buttons :-</b>
<code>[Button Text](buttonalert:This is an Alert Message)</code>"""
    AUTOFILTER_TXT = """<b>Help :-</b> <b>Auto Filter</b>
    
<b>You Can On or Off Auto Filter From Your Chat. 

<b>Commands and Usage :-</b>

• /autofilter - On/Off Filers in a Chat (Chat Admin 👨🏻‍✈️ Only)

Example :- <code>/autofilter on</code> Or <code>/autofilter off</code></b>

<b>NOTE :-</b>
<b>1. Make Me The 👨🏻‍✈️ Admin of Your Channel if it's Private.
2. Make Sure that Your Channel Doesn't Contains CAMRip, PreDVD, Porn and Fake Files 📂.
3. Forward the last Message to me with Quotes.
 I'll Add all the Files 📂 in that Channel to My Database.</b>"""
    CONNECTION_TXT = """<b>Help :-</b> <b>Connections</b>

<b>- Used to Connect Bot to PM for Managing Filters 
- it Helps To Avoid Spamming in Groups.</b>

<b>NOTE :-</b>
<b>1. Only 👨🏻‍✈️ Admins can Add a Connection.
2. Send</b> <code>/connect</code> <b>for Connecting Me To Your PM</b>

<b>Commands and Usage :</b>
<b>• /connect - Connect a Particular Chat to Your PM
• /disconnect - Disconnect From a Chat 
• /connections - List All Your Connections</b>"""
    EXTRAMOD_TXT = """<b>Help :-</b> <b>Extra Modules</b>

<b>NOTE :-</b>
<b>These are the Extra Features of Our <a href=https://t.me/UK_Movies_Bot><b>UK Movies Bot</b></a></b>

<b>Commands and Usage :</b>
<b>• /id - Get ID of a Specified User.
• /info - Get Information About a User.
• /imdb - Get the Movie 🎥 Information From IMDB Source.
• /search - Get the Movie 🎥 Information from Various Sources.
• /set_template - Set a New Custom IMDB Template For Individual Groups. (Chat Admin 👨🏻‍✈️ Only)

New Features ✨

• /font - Font is a Module For Make Your Text Stylish 🖊️
• /share - Reply with Any Text to Get Share Link 🔗
• /graph - Reply to a Photo or Video Under 5MB
• /text2speech - Reply with Text to Get Audio Speech 💬
• /alive - Check Bot Alive or Not
• /password - Generate Secret Password 🔑

YTDL Features  ✨

• /video - Download Video From YouTube with Any Link 🔗 (Auto Quality)
• /song - Download Song From YouTube with Song Name</b>"""

    ADMIN_TXT = """<b>Help :-</b> <b>👨🏻‍✈️ Admin Mods</b>

<b>NOTE :-</b>
<b>This Module only Works for My 👨🏻‍✈️ Admins</b>

<b>Commands and Usage :-</b>
<b>• /logs - to Get The Recent Errors
• /send - Send Message to Spacific User 🤵🏻 (Admin 👨🏻‍✈️ Only)
• /group_send - Send Message to Spacific Chat 🤵🏻 (Admin 👨🏻‍✈️ Only)
• /stats - to Get Status 📊 Of Files 📂 in Database.
• /status - to Get Status 📊 Of This Bot 🤖
• /delete - to Delete 🗑️ a Specific File 📂 From Database.
• /deleteall - to Delete 🗑️ to All Files 📂 From Database.
• /deletefiles - to Delete 🗑️ PreDVD and CAMRip Files 📂 From Database.
• /users - to Get List of My Users and IDs.
• /junk_users - Clear All Deleted Accounts & Blocked Accounts From Database.
• /chats - to Get List of The My Chats and IDs.
• /junk_chats - Clear Admin 👨🏻‍✈️ Removed Chats or Deactivated Chats on Database.
• /leave  - to Leave From a Chat.
• /disable  - to Disable a Chat.
• /ban  - to Ban a User.
• /unban  - to Unban a User.
• /channel - to Get List of Total Connected Channels 
• /broadcast - to Broadcast a Message to All Users 📊
• /group_broadcast - to Broadcast a Message to All Groups 👥
• /restart - to Restart The Bot 🤖 With Heroku</b>"""

    STATUS_TXT = """<b>🗃️ Total Files :-</b> <code>{}</code> <b>Files</b>\n
<b>👩🏻‍💻 Total Users :-</b> <code>{}</code> <b>Users</b>\n
<b>👥 Total Groups :-</b> <code>{}</code> <b>Groups</b>\n
<b>💾 Used Storage :-</b> <code>{}</code>\n
<b>🆓 Free Storage :-</b> <code>{}</code>"""

    LOG_TEXT_G = """<b>#New_Group</b>
    
<b>᚛› Group ⪼ {}</b>
<b>᚛› Group ID ⪼ <code>{}</code></b>
<b>᚛› Total Members ⪼ <code>{}</code></b>
<b>᚛› Added By ⪼ {}</b>
<b>᚛› From Bot ⪼ <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</a></b>
"""
    LOG_TEXT_P = """<b>#New_User</b>
    
<b>᚛› ID - <code>{}</code></b>
<b>᚛› Name - {}</b>
<b>᚛› From Bot ⪼ <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</a></b>
"""

TRANSLATED_MSG = """<b>Choose The Language From Here That I Want to Translate.👇</b>"""

REQ_TO_ADMIN = """<b>😒 Currently Unavailable to My Database or Not Released This Movie 🎥 ! We are Really Sorry for Inconvenience..!\n Have Patience..! Our Greatest 👨🏻‍✈️ Admins Will Upload This Movie 🎥 As Soon as Possible.!\n\nRequest to Our Greatest 👨🏻‍✈️ Admins</b>"""

CREDITS = """**Credits Here**"""
