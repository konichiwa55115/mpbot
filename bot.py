import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6032076608:AAEwM7ZpCKKXIdw5TVJVu5jxND2vklkog2U"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا فصل الموسيقا , فقط أرسل الفيديو هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.voice )
def _telegram_file(client, message):
  try: 
    with open("./downloads/entry", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار الفصل \n\n قال رسول الله ﷺ  لَيَكونَنَّ مِن أُمَّتي أقْوامٌ يَسْتَحِلُّونَ الحِرَ والحَرِيرَ، والخَمْرَ والمَعازِفَ، ولَيَنْزِلَنَّ أقْوامٌ إلى جَنْبِ عَلَمٍ، يَرُوحُ عليهم بسارِحَةٍ لهمْ، يَأْتِيهِمْ -يَعْنِي الفقِيرَ- لِحاجَةٍ، فيَقولونَ: ارْجِعْ إلَيْنا غَدًا، فيُبَيِّتُهُمُ اللَّهُ، ويَضَعُ العَلَمَ، ويَمْسَخُ آخَرِينَ قِرَدَةً وخَنازِيرَ إلى يَومِ القِيامَةِ. ( صحيح البخاري)', quote=True)
  file = message.voice
  file_path = message.download(file_name="entry")

    # Execute speech.py script with entry file
  subprocess.call(['ffmpeg', '-i',"./downloads/entry",'-q:a','0','-map','a',"result.mp3",'-y' ])
    # Upload transcription file to user
  with open("./result.mp3", 'rb') as f:
        bot.send_audio(message.chat.id, f)
  subprocess.call(['sudo','rm','-r',"./downloads/entry"]) 
  subprocess.call(['sudo','rm','-r',"entry.mp3"]) 
 
 
 

bot.run()
