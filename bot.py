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
    [InlineKeyboardButton("قص صوتية / فيديو ",callback_data="trim")],
    [InlineKeyboardButton("تسريع صوتية / فيديو ",callback_data="speedy")],
    [InlineKeyboardButton("كتم صوت الفيديو",callback_data="mute")],
     [InlineKeyboardButton("ضغط الصوتية ",callback_data="comp")],
          [InlineKeyboardButton("دمج صوتيات ",callback_data="audmerge")],
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

CHOOSE_UR_COMP_MODE = " اختر نمط الضغط \n كلما قل الرقم زاد الضغط و قل حجم الصوتية "
CHOOSE_UR_COMP_MODE_BUTTONS = [
    [InlineKeyboardButton("10k",callback_data="compmod1")],
     [InlineKeyboardButton("20k",callback_data="compmod2")],
     [InlineKeyboardButton("30k",callback_data="compmod3")],
     [InlineKeyboardButton("40k",callback_data="compmod4")],
     [InlineKeyboardButton("50k",callback_data="compmod5")]
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
CHOOSE_UR_FILESPED_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILESPED_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="speedfileaud")],
     [InlineKeyboardButton("فيديو ",callback_data="speedfilevid")]
]

CHOOSE_UR_SPEED_MODE = "اختر نمط التسريع "
CHOOSE_UR_SPEED_MODE_BUTTONS = [
    [InlineKeyboardButton("x1.25",callback_data="spd1")],
     [InlineKeyboardButton("x1.5 ",callback_data="spd2")],
     [InlineKeyboardButton("x1.75",callback_data="spd3")],
      [InlineKeyboardButton("x2",callback_data="spd4")]
]
CHOOSE_UR_MERGE = "أرسل الصوتية التالية  \n تنبيه / بعد الانتهاء من إرسال الصوتيات اضغط دمج الآن "
CHOOSE_UR_MERGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="mergenow")] ]


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
  global spdrateaud
  global mergdir
  mergdir = f"./downloads/{mp3file}"


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
             text = CHOOSE_UR_COMP_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
  elif  CallbackQuery.data == "compmod1":
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 10k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
    cmd(f''' unlink "{file_path}" && unlink "{mp3file}" ''')
  elif  CallbackQuery.data == "compmod2":
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 20k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
    cmd(f''' unlink "{file_path}" && unlink "{mp3file}" ''')
  elif  CallbackQuery.data == "compmod3":
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 30k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
    cmd(f''' unlink "{file_path}" && unlink "{mp3file}" ''')
  elif  CallbackQuery.data == "compmod4":
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 40k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
    cmd(f''' unlink "{file_path}" && unlink "{mp3file}" ''')
  elif  CallbackQuery.data == "compmod5":
    CallbackQuery.edit_message_text("جار الضغط ") 
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
  elif CallbackQuery.data == "mute":
    CallbackQuery.edit_message_text("جار الكتم")
    cmd(f'''ffmpeg -i "{file_path}" -c copy -an "{mp4file}"''')
    with open(mp4file, 'rb') as f:
             bot.send_document(user_id, f)
    cmd(f'''unlink "{mp4file}" && unlink "{file_path}"''')
  elif CallbackQuery.data == "speedy":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_SPEED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS)
        )

  elif CallbackQuery.data == "spd1":
    global spdratevid
    spdratevid = 0.8
    global spdrateaud
    spdrateaud = 1.25
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd2":
    spdratevid = 0.66666666666
    spdrateaud = 1.5
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd3":
    spdratevid = 0.57142857142
    spdrateaud = 1.75
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd4":
    spdratevid = 0.5
    spdrateaud = 2
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "speedfileaud":
    CallbackQuery.edit_message_text("جار التسريع")
    cmd(f'''ffmpeg -i {file_path} -filter:a "atempo={spdrateaud}" -vn {mp3file} -y ''')
    with open(mp3file, 'rb') as f:
             bot.send_audio(user_id, f)
    cmd(f'''unlink "{mp3file}" && unlink "{file_path}"''')
  elif CallbackQuery.data == "speedfilevid":
    CallbackQuery.edit_message_text("جار التسريع")
    cmd(f'''ffmpeg -i {file_path} -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" {mp4file} -y ''')
    with open(mp4file, 'rb') as f:
             bot.send_video(user_id, f)
    cmd(f'''unlink "{mp4file}" && unlink "{file_path}"''')
  elif CallbackQuery.data == "audmerge":
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mergdir}" -y ''')
    with open('list.txt','a') as f:
      f.write(f'''file '{mergdir}' \n''')
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_MERGE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
  elif CallbackQuery.data == "mergenow":
    CallbackQuery.edit_message_text("جار الدمج")   
    cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
         bot.send_audio(user_id, f)
    cmd(f'''rm list.txt && rm "{mp3file}" ''')
    shutil.rmtree('./downloads/') 






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
