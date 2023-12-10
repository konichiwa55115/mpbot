import os ,re
from pyrogram import Client, filters
import requests
from os import system as cmd
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

bot = Client(
    "pdfcompress",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E"
)


@bot.on_message(filters.private & filters.incoming & filters.document )
def _telegram_file(client, message):
 file = message
 file_path = message.download(file_name="./downloads/")
 filename = os.path.basename(file_path)
 user_id = message.from_user.id
        # Initialize the library
 PDFNet.Initialize("demo:1676040759361:7d2a298a03000000006027df7c81c9e05abce088e7286e8312e5e06886"); doc = PDFDoc(f"{file_path}")
        # Optimize PDF with the default settings
 doc.InitSecurityHandler()
        # Reduce PDF size by removing redundant information and
        # compressing data streams
 Optimizer.Optimize(doc)
 doc.Save(f"{filename}", SDFDoc.e_linearized)
 doc.Close()
 with open(filename, 'rb') as f:
         bot.send_document(user_id, f)
 cmd(f''' unlink "{filename}" ''')
 shutil.rmtree('./downloads/') 

        
bot.run()
