import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5848326557:AAGHzvPErt9hr6NFYn7TNDOaXQiVXvR213c"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت الصوتيات , فقط أرسل الفيديو أو الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video )
def _telegram_file(client, message):

  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية أو الفيديو بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار المعالجة ', quote=True)
  file = message.voice
  file_path = message.download(file_name="./downloads/")
  head, tail = os.path.split(file_path)
  subprocess.call(['ffmpeg', '-i', file_path,'-q:a','0','-map','a',tail+".mp3",'-y' ])
    # Upload transcription file to user
  with open(tail+".mp3", 'rb') as f:
        bot.send_audio(message.chat.id, f)
  subprocess.call(['sudo','rm','-r',head]) 
  subprocess.call(['sudo','rm','-r',tail+".mp3"]) 

 
 

bot.run()
