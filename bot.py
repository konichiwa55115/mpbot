import os
from pyrogram import Client, filters
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
import shutil
bot = Client(
    "audiobot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6032076608:AAGhqffAlibHd7pipzA3HR2-0Ca3sDFlmdI"
)

CHOOSE_UR_AUDIO_MODE = "اختر العملية  التي تريد "
CHOOSE_UR_AUDIO_MODE_BUTTONS = [
    [InlineKeyboardButton("تضخيم صوتية / فيديو ",callback_data="amplifyaud")],
     [InlineKeyboardButton("ضغط الصوتية ",callback_data="comp")],
          [InlineKeyboardButton("قص صوتية / فيديو ",callback_data="trim")],
     [InlineKeyboardButton("التحويل إلى mp3 ",callback_data="conv")],
     [InlineKeyboardButton("إعادة التسمية ",callback_data="renm")]

]

CHOOSE_UR_AMPLE_MODE = "اختر نمط التضخيم "
CHOOSE_UR_AMPLE_MODE_BUTTONS = [
    [InlineKeyboardButton("5db",callback_data="mod1")],
     [InlineKeyboardButton("10db",callback_data="mod2")],
     [InlineKeyboardButton("15db",callback_data="mod3")],
     [InlineKeyboardButton("20db",callback_data="mod4")],
     [InlineKeyboardButton("25db",callback_data="mod5")]
]
CHOOSE_UR_FILE_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILE_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="aud")],
     [InlineKeyboardButton("فيديو ",callback_data="vid")]
]

CHOOSE_UR_FILETRIM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILETRIM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audtrim")],
     [InlineKeyboardButton("فيديو ",callback_data="vidtrim")]
     ]
CHOOSE_UR_FILERENM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILERENM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audrenm")],
     [InlineKeyboardButton("فيديو ",callback_data="vidrenm")],
     [InlineKeyboardButton("وثيقة",callback_data="docrenm")]
]

@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document )
def _telegram_file(client, message):
  global user_id
  user_id = message.from_user.id
  global file
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  global filename
  filename = os.path.basename(file_path)
  global nom
  global ex
  nom,ex = os.path.splitext(filename)
  global mp4file
  mp4file = f"{nom}.mp4"
  global mp3file
  mp3file = f"{nom}.mp3"
  message.reply(
             text = CHOOSE_UR_AUDIO_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIO_MODE_BUTTONS)

        )




@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global amplemode 
  if CallbackQuery.data == "amplifyaud":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_AMPLE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS)

        )

  elif CallbackQuery.data == "comp":
   CallbackQuery.edit_message_text(
      
      "جار الضغط"
   )     
   cmd(f''' ffmpeg -i "{file_path}" -b:a 50k "{mp3file}" -y ''' )
   with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
   cmd(f''' unlink "{file_path}" && unlink "{mp3file}" ''')
  elif CallbackQuery.data == "conv" :
   CallbackQuery.edit_message_text(
      
      "جار التحويل "
   ) 
   cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
   with open(mp3file, 'rb') as f:
        bot.send_audio(user_id, f)
   cmd(f'''unlink "{file_path}" && unlink "{mp3file}" ''')
  elif CallbackQuery.data == "trim" :
   file.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))
   CallbackQuery.edit_message_text(
      
      "👇"
   ) 
  elif CallbackQuery.data == "mod1":
      amplemode = 5
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod2":
      amplemode = 10
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod3":
      amplemode = 15
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod4" :
      amplemode = 20
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod5":
      amplemode = 25
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )

  elif CallbackQuery.data == "aud":
    CallbackQuery.edit_message_text(
     "جار التضخيم "
      )
    cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{filename}"''')
    with open(filename, 'rb') as f:
        bot.send_audio(user_id, f)
    cmd(f'''unlink "{filename}" && unlink "{file_path}"''')
  
  elif CallbackQuery.data == "vid":
    CallbackQuery.edit_message_text(
     "جار التضخيم "
      )
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./downloads/{mp3file}" -y ''')
    cmd(f'''ffmpeg -i "./downloads/{mp3file}" -filter:a volume={amplemode}dB "{mp3file}"''')
    cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{filename}"''')
    with open(filename, 'rb') as f:
        bot.send_video(user_id, f)
    cmd(f'''unlink "{filename}" && unlink "{file_path}"''')    
  elif CallbackQuery.data == "audtrim":
    CallbackQuery.edit_message_text(
     "جار القص"
      )  
    cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
            bot.send_audio(user_id, f)
    cmd(f'''unlink "{file_path}" && unlink "{mp3file}"''')
  elif CallbackQuery.data == "vidtrim":
    CallbackQuery.edit_message_text(
     "جار القص"
      )  
    cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -to {end_point} -c copy "{mp4file}" -y ''')
    with open(mp4file, 'rb') as f:
            bot.send_video(user_id, f)
    cmd(f'''unlink "{file_path}" && unlink "{mp4file}" ''')
  elif CallbackQuery.data == "renm":
    file.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))
    CallbackQuery.edit_message_text(
      
      "👇"
   ) 

  elif CallbackQuery.data == "audrenm":
    CallbackQuery.edit_message_text("👇")
    with open(newfile, 'rb') as f:
             bot.send_audio(user_id, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "vidrenm":
    CallbackQuery.edit_message_text("👇")
    with open(newfile, 'rb') as f:
             bot.send_video(user_id, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "docrenm":
    CallbackQuery.edit_message_text("👇")
    with open(newfile, 'rb') as f:
             bot.send_document(user_id, f)
    cmd(f'''unlink "{newfile}" ''')


@bot.on_message(filters.private & filters.reply & filters.regex('/'))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          endstart = message.text ;await message.delete()
          global strt_point
          global end_point
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
          await message.reply(
             text = CHOOSE_UR_FILETRIM_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILETRIM_MODE_BUTTONS)

        )
@bot.on_message(filters.private & filters.reply )
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          newname = message.text ;await message.delete()
          global newfile
          newfile = f"{newname}{ex}"
          cmd(f'''mv "{file_path}" "{newfile}"''')
          await message.reply(
             text = CHOOSE_UR_FILERENM_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILERENM_MODE_BUTTONS)

           )
        
bot.run()
