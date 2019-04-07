from mysql import connector
import mysql
from PIL import Image
import requests
from io import BytesIO




def getI():
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
    
    image = Image.open("tmp_img\\nst\\"+img_name)
    image1 = Image.open("tmp_img\\nst\\"+img_name_style)
    #image.show()
    #image1.show()
    return img_name,img_name_style
