from mysql import connector
import mysql
from PIL import Image
import requests
from io import BytesIO

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="ml_void_hack"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users WHERE id = (SELECT MAX(id) FROM users)")


myresult = mycursor.fetchall()
print(myresult[0][0])
print(myresult[0][1])
img_name = myresult[0][0]
img_name_style=myresult[0][1]

content_path = Image.open("C:\\wamp64\\www\\MLAIVoidhack\\img\\"+img_name)
style_path= Image.open("C:\\wamp64\\www\\MLAIVoidhack\\img\\"+img_name_style)


