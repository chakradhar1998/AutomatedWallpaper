# In[299]:
import requests
import random
import os
import wget
import subprocess
# In[]
def connection():
    try:
        response=requests.get("https://picsum.photos/5000/3700")
        return response.url
    except requests.exceptions.HTTPError:
        subprocess.Popen(['notify-send', "connection issue"])
    except requests.exceptions.InvalidSchema:
        subprocess.Popen(['notify-send', "invalid url"])

# In[]

def download_image(a):
    filesra=os.listdir(os.getcwd())
    for pic in filesra:
        if pic.endswith('.jpg'):
            os.remove(pic)
    try:
        file_name=wget.download(a)
    except requests.exceptions.HTTPError:
        print(('some connection issue occurred'))

# In[]
def setwallp():
    path='/home/chakradhar/Documents/python'
    chak="gsettings set org.gnome.desktop.background picture-uri "
    filesra=os.listdir(path)
    kra_list=[]
    for pic in filesra:
        if pic.endswith('.jpg'):
            kra=f"'file:///home/chakradhar/Documents/python/{pic}'"
            theimage=pic
    os.system(chak+kra)
# In[]
a=connection()

# In[]
download_image(a)

# In[]
setwallp()
# %%
