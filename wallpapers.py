# In[299]:
import requests
import random
import os
import wget
# In[]
def connection():
    try:
        response=requests.get("https://picsum.photos/5000/3700")
        response.raise_for_status()
        return response.url
    except requests.exceptions.HTTPError:
        print('please enter correct url')



def download_image(a):
    filesra=os.listdir(os.getcwd())
    for pic in filesra:
        if pic.endswith('.jpg'):
            os.remove(pic)
    try:
        file_name=wget.download(a)
    except requests.exceptions.HTTPError:
        print(('some connection issue occurred'))


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
    #os.remove(theimage)

# In[]
a=connection()

# In[]
download_image(a)

# In[]
setwallp()