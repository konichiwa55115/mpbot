from pyrogram import Client, filters 
import os ,re , random ,shutil,asyncio ,pytesseract,requests  
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
import pypdfium2 as pdfium
from yt_dlp import YoutubeDL
from PyPDF2 import PdfWriter, PdfReader
from pypdf import PdfMerger
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
from pathlib import Path
from urllib.parse import urlparse, unquote
ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
bot = Client(
    "audiobot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6306753444:AAFnoiusUbny-fpy4xxZWYqGNh_c7yOioW8"
)
#6032076608:AAGhqffAlibHd7pipzA3HR2-0Ca3sDFlmdI 
#5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E

CHOOSE_UR_AUDIO_MODE = "اختر العملية  التي تريد "
CHOOSE_UR_AUDIO_MODE_BUTTONS = [
    
    [InlineKeyboardButton("تضخيم صوتية / فيديو ",callback_data="amplifyaud"),InlineKeyboardButton("قص صوتية / فيديو ",callback_data="trim")],
[InlineKeyboardButton("تسريع صوتية / فيديو ",callback_data="speedy"),InlineKeyboardButton("تحويل صوتية / فيديو ",callback_data="conv")], 
    [InlineKeyboardButton("كتم صوت الفيديو",callback_data="mute"), InlineKeyboardButton("ضغط الصوتية ",callback_data="comp")],
    [InlineKeyboardButton("تقسيم الصوتية ",callback_data="splitty"),InlineKeyboardButton("دمج صوتيات ",callback_data="audmerge")],
    [InlineKeyboardButton("تغيير الصوت",callback_data="voicy"),InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs")], 
    [InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid"),InlineKeyboardButton("تفريغ صوتية",callback_data="transcribe")],
    [InlineKeyboardButton("إعادة التسمية ",callback_data="renm"),InlineKeyboardButton("OCR صور",callback_data="OCR")],
    [InlineKeyboardButton("تفريغ pdf",callback_data="pdfOCR"),InlineKeyboardButton("ضغط pdf",callback_data="pdfcompress")],
    [InlineKeyboardButton("دمج pdf",callback_data="pdfmerge"),InlineKeyboardButton("قص pdf ",callback_data="pdftrim")],
     [InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch"),InlineKeyboardButton("titled",callback_data="titled")]
    
]
CHOOSE_UR_DL_MODE = "اختر نمط التنزيل "
CHOOSE_UR_DL_MODE_BUTTONS = [
    [InlineKeyboardButton("VIDEO 360P",callback_data="vid360")],
    [InlineKeyboardButton("VIDEO 720P ",callback_data="vid720")],
    [InlineKeyboardButton("AUDIO",callback_data="auddl")],
    
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
CHOOSE_UR_PDFMERGE_MODE = " بعد الانتهاء من إرسال الملفات اضغط دمج الآن "
CHOOSE_UR_PDFMERGE_MODE_BUTTONS = [
  [InlineKeyboardButton("دمج الآن ",callback_data="pdfmergenow")]
]
CHOOSE_UR_MERGE = "أرسل الصوتية التالية  \n تنبيه / بعد الانتهاء من إرسال الصوتيات اضغط دمج الآن "
CHOOSE_UR_MERGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="mergenow")] ]

CHOOSE_UR_CONV_MODE = "اختر نمط التحويل"
CHOOSE_UR_CONV_MODE_BUTTONS = [
    [InlineKeyboardButton("تحويل صوتية/ فيديو إلى mp3",callback_data="audconv")],
     [InlineKeyboardButton("تحويل صوتية/ فيديو إلى m4a",callback_data="audconvm4a")],
    [InlineKeyboardButton("تحويل فيديو إلى mp4 ",callback_data="vidconv")]
]
CHOOSE_UR_SUBS_MODE = '''اختر ما يناسب'''
CHOOSE_UR_SUBS_MODE_BUTTONS = [
    [InlineKeyboardButton("هذا الفيديو",callback_data="thisisvid")], [InlineKeyboardButton("إبدال الآن",callback_data="subsnow")]]
CHOOSE_UR_MON_MODE = '''اختر ما يناسب'''
CHOOSE_UR_MON_MODE_BUTTONS = [
    [InlineKeyboardButton("هذه الصورة",callback_data="thisisimage")], [InlineKeyboardButton("منتجة الآن",callback_data="montagnow")]]
CHOOSE_UR_RESO_MODE = '''اختر ما يناسب'''
CHOOSE_UR_RESO_MODE_BUTTONS = [
    [InlineKeyboardButton("فيديو اعتيادي",callback_data="normalvideo")], [InlineKeyboardButton("YT Short",callback_data="ytshort")]]

@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)

@bot.on_message(filters.command('setbucket') & filters.text & filters.private)
def command9(bot,message):
  global bucketname
  bucketname = message.text.split("setbucket", maxsplit=1)[1]
  bucketname = bucketname.replace(" ", "")
  message.reply_text("تم ضبط المعرف ")

@bot.on_message(filters.command('ytdl') & filters.text & filters.private)
def command20(bot,message):
     global yt_id , ytlink
     ytlink = message.text.split("ytdl", maxsplit=1)[1].replace(" ", "")
     yt_id = message.from_user.id
     message.reply(
             text = CHOOSE_UR_DL_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_DL_MODE_BUTTONS)

        )

@bot.on_message(filters.command('yttransy') & filters.text & filters.private)
def command4(bot,message):
     url = message.text.split("yttransy ", maxsplit=1)[1]
     yttransyid = message.from_user.id
     temptxt = "res.txt"
     cmd(f'''yt-dlp --flat-playlist -i --print-to-file url yttransy.txt {url}''')
     cmd(f'''wc -l < yttransy.txt > "{temptxt}"''')
     with open(temptxt, 'r') as file:
        temp = file.read().rstrip('\n') 
     numbofvid = int(temp) + 1
     os.remove(temptxt)
     for i in range(1,numbofvid):
         cmd(f'sed -n {i}p yttransy.txt > res.txt')
         with open('res.txt', 'r') as file:
           link = file.read().rstrip('\n')  
         with YoutubeDL() as ydl: 
          info_dict = ydl.extract_info(f'{link}', download=False)
          video_url = info_dict.get("url", None)
          video_id = info_dict.get("id", None)
          video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "") 
          mp3file =   f"{video_title}.mp3"
          txtresfile = f"{video_title}.txt"
         cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}"  "{link}"''')
         cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{mp3file}" "{txtresfile}"''')
         with open(txtresfile, 'rb') as f:
           bot.send_document(yttransyid, f,caption=video_title)
         os.remove(txtresfile)
         os.remove(mp3file)
         os.remove(temptxt)
     os.remove("yttransy.txt")



@bot.on_message(filters.command('upld') & filters.text & filters.private)
def command2(bot,message):
     url = message.text.split("upld ", maxsplit=1)[1]
     upld_id = message.from_user.id
     a= urlparse(url).path 
     url_parsed = urlparse(url)
     a = unquote(url_parsed.path)
     filename =a.split("/")[-1] 
     if filename.endswith('.mp3' or '.m4a' or '.ogg') :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
        bot.send_audio(upld_id,f)
     elif filename.endswith('.mp4' or '.mkv' or '.wmv') :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
       bot.send_video(upld_id,f)
     else :
      cmd(f'''wget -O "{filename}" "{url}"''')
      with open(filename,'rb') as f : 
       bot.send_document(upld_id,f)
@bot.on_message(filters.command('clear') & filters.private)
def command2(bot,message):
    cmd('''rm list.txt ''')
    
@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo )
def _telegram_file(client, message):
  global user_id ,nepho,file_path,filename,nom,ex,mp4file,mp3file,m4afile,spdrateaud,mergdir,trimdir,result
  user_id = message.from_user.id
  nepho = message 
  x = message.download(file_name="./downloads/")
  file_path = x.replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
  cmd(f'''mv "{x}" "{file_path}"''')
  filename = os.path.basename(file_path)
  print(filename)
  nom,ex = os.path.splitext(filename)
  mp4file = f"{nom}.mp4"
  mp3file = f"{nom}.mp3"
  m4afile = f"{nom}.m4a"
  mergdir = f"./mergy/{mp3file}"
  trimdir = f"./trimmo/{mp3file}" 
  result = f"{nom}.txt"
  message.reply(
             text = CHOOSE_UR_AUDIO_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIO_MODE_BUTTONS)

        )


      
@bot.on_callback_query()
async def callback_query(CLIENT,CallbackQuery):
  global amplemode 
  if CallbackQuery.data == "amplifyaud":
     await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_AMPLE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS)

        )

  elif CallbackQuery.data == "comp":
   await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_COMP_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
  elif  CallbackQuery.data == "compmod1":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    aid = user_id
    cmd(f''' ffmpeg -i "{file_path}" -b:a 10k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
        await bot.send_audio(aid, f)
   
    os.remove(file_path) 
    os.remove(mp3file) 
  elif  CallbackQuery.data == "titled":
      cmd(f'''mv "{file_path}" "{filename}"''')
      with open(filename, 'rb') as f:
        await bot.send_document(user_id, f)
      await CallbackQuery.edit_message_text("تم الإرسال  ") 
      cmd(f'''rm "{filename}"''')

  elif  CallbackQuery.data == "voicy":   
    await CallbackQuery.edit_message_text("جار تغيير الصوت ") 
    bid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -af asetrate=44100*0.9,aresample=44100,atempo=1/0.9 "{mp3file}"''')
    with open(mp3file, 'rb') as f:
         await bot.send_audio(bid, f)
   
    os.remove(file_path) 
    os.remove(mp3file) 


  elif  CallbackQuery.data == "thisisvid":
     cmd(f'''mv "{file_path}" "./downloads/subsvid.mp4" ''')
     await CallbackQuery.edit_message_text("الآن أرسل الصوت الجديد ثم اختر إبدال الآن") 
  elif  CallbackQuery.data == "thisisimage":
     cmd(f'''mv "{file_path}" "./downloads/imagetovid.jpg" ''')
     await CallbackQuery.edit_message_text("الآن أرسل الصوت  ثم اختر منتجة الآن") 

  elif  CallbackQuery.data == "subs":
     await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_SUBS_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SUBS_MODE_BUTTONS)

        )
  elif  CallbackQuery.data == "imagetovid":
     await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_MON_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MON_MODE_BUTTONS)

        )
  elif  CallbackQuery.data == "subsnow":
      await CallbackQuery.edit_message_text("جار الإبدال ") 
      cid = user_id
      cmd(f'''ffmpeg -i "./downloads/subsvid.mp4" -i "{file_path}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
      with open(mp4file, 'rb') as f:
         await bot.send_video(cid, f)
      os.remove(file_path) 
      os.remove(mp4file) 


  elif  CallbackQuery.data == "montagnow":
      global thisismontagaudio
      thisismontagaudio = file_path
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_RESO_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_RESO_MODE_BUTTONS))
  elif CallbackQuery.data == "normalvideo":
      await CallbackQuery.edit_message_text("جار المنتجة ") 
      did = user_id
      cmd(f'''ffmpeg -i "{thisismontagaudio}" -q:a 0 -map a "./downloads/temp{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "./downloads/imagetovid.jpg" -i "./downloads/temp{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      with open(mp4file, 'rb') as f:
         await bot.send_video(did, f)
      os.remove(file_path) 
      os.remove(mp4file) 
  elif CallbackQuery.data == "ytshort":
      await CallbackQuery.edit_message_text("جار المنتجة ") 
      did = user_id
      cmd(f'''ffmpeg -i "{thisismontagaudio}" -q:a 0 -map a "./downloads/temp{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "./downloads/imagetovid.jpg" -i "./downloads/temp{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1080:1920 "{mp4file}"''')
      with open(mp4file, 'rb') as f:
         await bot.send_video(did, f)
      os.remove(file_path) 
      os.remove(mp4file) 
  elif  CallbackQuery.data == "compmod2":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 20k "{mp3file}" -y ''' )
    eid = user_id
    with open(mp3file, 'rb') as f:
         await bot.send_audio(eid, f)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif  CallbackQuery.data == "compmod3":
    fid = user_id
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 30k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         await bot.send_audio(fid, f)
    os.remove(file_path) 
    os.remove(mp3file)  

  elif  CallbackQuery.data == "compmod4":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    gid = user_id
    cmd(f''' ffmpeg -i "{file_path}" -b:a 40k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         await bot.send_audio(gid, f)
    os.remove(file_path) 
    os.remove(mp3file) 

  elif  CallbackQuery.data == "compmod5":
    hid = user_id
    await CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 50k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
        await bot.send_audio(hid, f)
    
    os.remove(file_path) 
    os.remove(mp3file) 

  elif CallbackQuery.data == "conv" :
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_CONV_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_CONV_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "audconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   iid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
   with open(mp3file, 'rb') as f:
       await  bot.send_audio(iid, f)
   os.remove(file_path) 
   os.remove(mp3file) 
  elif CallbackQuery.data == "audconvm4a" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   lamid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -c:a aac -b:a 192k "{m4afile}" -y ''')
   with open(m4afile, 'rb') as f:
        await bot.send_document(lamid, f)
   os.remove(file_path) 
   os.remove(m4afile) 

  elif CallbackQuery.data == "vidconv" :
   await CallbackQuery.edit_message_text("جار التحويل " ) 
   jid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -codec copy "{mp4file}" -y ''')
   with open(mp4file, 'rb') as f:
       await bot.send_video(jid, f)
   
   os.remove(file_path) 
   os.remove(mp4file) 

  elif CallbackQuery.data == "trim" :
   await nepho.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))
   await CallbackQuery.edit_message_text("👇") 
  elif CallbackQuery.data == "mod1":
      amplemode = 5
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod2":
      amplemode = 10
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod3":
      amplemode = 15
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod4" :
      amplemode = 20
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS))
  elif CallbackQuery.data == "mod5":
      amplemode = 25
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS) )

  elif CallbackQuery.data == "aud":
    await CallbackQuery.edit_message_text("جار التضخيم ")
    kid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{filename}"''')
    with open(filename, 'rb') as f:
        await bot.send_audio(kid, f)
     
    os.remove(file_path) 
    os.remove(filename) 

  elif CallbackQuery.data == "vid":
    await CallbackQuery.edit_message_text("جار التضخيم " )
    lid = user_id
    cmd('mkdir tempdir')
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./tempdir/{mp3file}" -y ''')
    cmd(f'''ffmpeg -i "./downloads/{mp3file}" -filter:a volume={amplemode}dB "{mp3file}"''')
    cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{filename}"''')
    with open(filename, 'rb') as f:
       await bot.send_video(lid, f) 
    os.remove(file_path) 
    os.remove(filename) 
    shutil.rmtree("./tempdir/")

  elif CallbackQuery.data == "audtrim":
    await CallbackQuery.edit_message_text("جار القص")  
    qid = user_id
    cmd(f'''mkdir trimmo''')  
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{trimdir}" -y ''')
    cmd(f'''ffmpeg -i "{trimdir}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
        await  bot.send_audio(qid, f)
    shutil.rmtree('./trimmo/') 
    os.remove(file_path) 
    os.remove(mp3file) 
      
  elif CallbackQuery.data == "vidtrim":
    await CallbackQuery.edit_message_text("جار القص")  
    rid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -strict -2 -to {end_point} -c:a aac -codec:v h264 -b:v 1000k "{mp4file}" -y ''')
    with open(mp4file, 'rb') as f:
           await bot.send_video(rid, f)
   
    os.remove(file_path) 
    os.remove(mp4file) 
  elif CallbackQuery.data == "renm":
    await nepho.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))
    await CallbackQuery.edit_message_text("👇") 
  elif CallbackQuery.data == "audrenm":
    await CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
        await  bot.send_audio(aid, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "vidrenm":
    await CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
           await  bot.send_video(aid, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "docrenm":
    await CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
          await   bot.send_document(aid, f)
    os.remove(newfile)
  elif CallbackQuery.data == "transcribe":
    try: 
      with open('transcription.txt', 'r') as fh:
        if os.stat('transcription.txt').st_size == 0: 
            pass
        else:
            CallbackQuery.edit_message_text("هناك عملية تفريغ تتم الآن")
            return
    except FileNotFoundError: 
      pass  
    await CallbackQuery.edit_message_text("جار التفريغ")
    finalid = user_id
    finalnom = result
    finalmp3 = mp3file
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')  
    cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{finalmp3}" "transcription.txt" ''')
    cmd(f'''mv transcription.txt "{finalnom}"''')
    with open(finalnom, 'rb') as f:
        await bot.send_document(finalid, f)
    await CallbackQuery.edit_message_text("تم التفريغ ✅  ")   
    os.remove(file_path) 
    os.remove(finalmp3) 
    os.remove(finalnom) 


    
  elif CallbackQuery.data == "mute":
    await CallbackQuery.edit_message_text("جار الكتم")
    aid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -c copy -an "{mp4file}"''')
    with open(mp4file, 'rb') as f:
          await   bot.send_document(aid, f)
    os.remove(file_path) 
    os.remove(mp4file) 



  elif CallbackQuery.data == "speedy":
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_SPEED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS)
        )

  elif CallbackQuery.data == "spd1":
    global spdratevid
    spdratevid = 0.8
    global spdrateaud
    spdrateaud = 1.25
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd2":
    spdratevid = 0.66666666666
    spdrateaud = 1.5
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd3":
    spdratevid = 0.57142857142
    spdrateaud = 1.75
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd4":
    spdratevid = 0.5
    spdrateaud = 2
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "speedfileaud":
    await CallbackQuery.edit_message_text("جار التسريع")
    aid = user_id
    cmd(f'''ffmpeg -i {file_path} -filter:a "atempo={spdrateaud}" -vn {mp3file} -y ''')
    with open(mp3file, 'rb') as f:
          await   bot.send_audio(aid, f) 
    os.remove(file_path) 
    os.remove(mp3file) 
  
  elif CallbackQuery.data == "vid360":
    await CallbackQuery.edit_message_text("جار التنزيل")
    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
          
    cmd(f'''yt-dlp -f 18 -ciw  -o "{video_title}.mp4" "{ytlink}"''')
    with open(f'''{video_title}.mp4''', 'rb') as f:
        await  bot.send_video(yt_id, f,caption=video_title)
    cmd(f'''rm "{video_title}.mp4" ''' ) 
  elif CallbackQuery.data == "vid720":
    await CallbackQuery.edit_message_text("جار التنزيل")
    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
    cmd(f'''yt-dlp -f 22 -ciw  -o "{video_title}.mp4" "{ytlink}"''')
    with open(f'''{video_title}.mp4''', 'rb') as f:
        await   bot.send_video(yt_id, f,caption=video_title)
    cmd(f'''rm "{video_title}.mp4" ''' ) 
  elif CallbackQuery.data == "auddl":
    await CallbackQuery.edit_message_text("جار التنزيل")
    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
    cmd(f'''yt-dlp -ciw  --extract-audio --audio-format mp3  -o "{video_title}.mp3"  "{ytlink}"''')
    with open(f'''{video_title}.mp3''', 'rb') as f:
       await   bot.send_audio(yt_id, f,caption=video_title)
    cmd(f'''rm "{video_title}.mp3" ''' ) 

  elif CallbackQuery.data == "speedfilevid":
    await CallbackQuery.edit_message_text("جار التسريع")
    aid = user_id
    cmd(f'''ffmpeg -i {file_path} -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" {mp4file} -y ''')
    with open(mp4file, 'rb') as f:
         await    bot.send_video(aid, f)
    
    os.remove(file_path) 
    os.remove(mp4file) 

  elif CallbackQuery.data == "audmerge":
    cmd(f'''mkdir mergy''')
    mp3merge = f"{nom}{random.randint(0,100)}.mp3"
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3merge}" -y ''')
    print(mp3merge)
    shutil.rmtree('./downloads/') 
    with open('list.txt','a') as f:
      f.write(f'''file '{mp3merge}' \n''')
    await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_MERGE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
  elif CallbackQuery.data == "mergenow":
    await CallbackQuery.edit_message_text("جار الدمج") 
    aid = user_id  
    cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
      await   bot.send_audio(aid, f)
    cmd(f'''rm list.txt "{mp3file}" ''')
    shutil.rmtree('./mergy/') 
  elif CallbackQuery.data == "splitty":
    await CallbackQuery.edit_message_text("جار التقسيم") 
    aid = user_id 
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a mod.mp3 -y''')
    cmd(f'mkdir parts')
    cmd(f'''ffmpeg -i "mod.mp3" -f segment -segment_time 300 -c copy "./parts/{nom}%09d.wav" -y''')
    dir_path = "./parts/"
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
    if numbofitems<10 :
        
     coca=0
     while (coca < numbofitems): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
              await bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1 
    else :
     coca=0 
     while (coca < 10): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
              await bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1        
     coca=10
     while (coca < numbofitems ): 
             pathy=f"./parts/{nom}0000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
              await  bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1                                      
    await shutil.rmtree('./parts/') 
    os.remove("mod.mp3") 
    os.remove(file_path) 
    
  elif CallbackQuery.data == "OCR":
   
    aid = user_id
    await CallbackQuery.edit_message_text("جار التفريغ")
    lang_code = "ara"
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
    dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
    path = os.path.join(dirs, f"{lang_code}.traineddata")
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    text = pytesseract.image_to_string(file_path, lang=f"{lang_code}")
    textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
    await nepho.reply(textspaced[:-1], quote=True, disable_web_page_preview=True)
    os.remove(file_path) 
  elif CallbackQuery.data == "pdfOCR":
    try: 
      with open('final.txt', 'r') as fh:
        if os.stat('final.txt').st_size == 0: 
            pass
        else:
            await CallbackQuery.edit_message_text("هناك تفريغ يتم الآن ") 
            return
    except FileNotFoundError: 
     pass  
    aid = user_id
    await CallbackQuery.edit_message_text("جار التفريغ")
    cmd('mkdir temp')
    pdf = pdfium.PdfDocument(file_path)
    n_pages = len(pdf)
    for page_number in range(n_pages):
     page = pdf.get_page(page_number)
     pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
     pil_image.save(f"./temp/image_{page_number+1}.png")
    shutil.rmtree('./downloads/') 
    os.remove(file_path) 
    count = 0
    for path in os.listdir("./temp/"):
                if os.path.isfile(os.path.join("./temp/", path)):
                            count += 1
                            numbofitems=count
    coca=1
    final = numbofitems 
    while (coca < final): 
     cmd(f'''sh textcleaner -g "./temp/image_{coca}.png" temp.png ''')
     lang_code = "ara"
     data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
     dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
     path = os.path.join(dirs, f"{lang_code}.traineddata")
     data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
     open(path, 'wb').write(data.content)
     text = pytesseract.image_to_string(f"temp.png" , lang=f"{lang_code}")
     textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
     with open("final.txt",'a') as f:
      f.write(f'''{textspaced} \n''')
     coca +=1
    cmd(f'''mv final.txt "{result}"''')
    with open(result, 'rb') as f:
        await bot.send_document(aid, f)
    shutil.rmtree('./temp/') 
    cmd(f'''rm "{result}"''')
  elif CallbackQuery.data == "pdfcompress":
      await CallbackQuery.edit_message_text("جار الضغط")
      PDFNet.Initialize("demo:1676040759361:7d2a298a03000000006027df7c81c9e05abce088e7286e8312e5e06886"); doc = PDFDoc(f"{file_path}")
      doc.InitSecurityHandler()
      Optimizer.Optimize(doc)
      doc.Save(f"{filename}", SDFDoc.e_linearized)
      doc.Close()
      with open(filename, 'rb') as f:
        await bot.send_document(user_id, f)
      os.remove(file_path) 
      os.remove(filename) 
  elif CallbackQuery.data == "pdfmerge":
      pdfdir = f"pdfmerge/{filename}"
      cmd("mkdir pdfmerge")
      cmd(f'''mv "{file_path}" ./pdfmerge/''')
      with open('pdfy.txt','a') as f:
       f.write(f'''{pdfdir} \n''')  
      await CallbackQuery.edit_message_text(
             text = CHOOSE_UR_PDFMERGE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_PDFMERGE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "pdfmergenow":
      await CallbackQuery.edit_message_text("جار الدمج")
      pdfs = []
      with open("pdfy.txt", "r") as file:
       for line in file:
        pdfs.append(line.strip())
      merger = PdfMerger()
      for pdf in pdfs:
       merger.append(pdf)
      pdfmerged = f"{filename}.pdf"
      merger.write(pdfmerged)
      merger.close()
      with open(pdfmerged,'rb') as f:
        await  bot.send_document(user_id,f)
      shutil.rmtree("./pdfmerge/")
      cmd(f'''rm "{pdfmerged}" pdfy.txt''')

  elif CallbackQuery.data == "pdftrim":
      await CallbackQuery.edit_message_text("👇")
      await nepho.reply_text(" الآن أرسل نقطة البداية والنهاية بهذه الصورة \n start-end ",reply_markup=ForceReply(True))
  elif CallbackQuery.data == "upldarch":
      if user_id==6234365091 :
         await CallbackQuery.edit_message_text("جار الرفع")
         cmd(f'''rclone copy '{file_path}' 'myarchive':"{bucketname}"''')
         os.remove(file_path)
         await CallbackQuery.edit_message_text("تم الرفع")
      else :
         await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
         
      





@bot.on_message(filters.private & filters.reply & filters.regex('/'))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          nepho.delete()
          endstart = message.text ;await message.delete()
          global strt_point
          global end_point
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
          await message.reply(
             text = CHOOSE_UR_FILETRIM_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILETRIM_MODE_BUTTONS)

        )
@bot.on_message(filters.private & filters.reply & filters.regex("-"))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          pstartpend = message.text ;await message.delete()
          global pdfstrt_point
          global pdfend_point
          startend = re.split('-',pstartpend)
          pdfstrt_point=int(startend[0])
          pdfend_point = int(startend[1])
          pages = (pdfstrt_point, pdfend_point)
          reader = PdfReader(file_path)
          writer = PdfWriter()
          page_range = range(pages[0], pages[1] + 1)
          for page_num, page in enumerate(reader.pages, 1):
           if page_num in page_range:
            writer.add_page(page)
           with open(filename, 'wb') as out:
            writer.write(out)
          with open(filename,'rb') as f : 
            await bot.send_document(user_id,f)
          os.remove(file_path) 
          os.remove(filename)
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
