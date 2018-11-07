import requests
from bs4 import BeautifulSoup as bs
import os
#URL for Image 
url = "https://pixabay.com/en/photos/?q=code&hp=&image_type=all&order=popular&cat=&min_width=&min_height="

#Downloading the Page for Scraping
page = requests.get(url)
soup = bs(page.text,"html.parser")

#Locating all the Images with <img> tag
image_tag = soup.findAll("img")

#Creating a Directory to Store Pictures the we Scrap
dir_name = "pictures"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

#This is for Creating and Appending the Title for the Images
title_file_name = "titles"
title_save_file = "titles.txt"
if not os.path.exists(os.path.join(dir_name,title_file_name)):
    os.mkdir(title_file_name)
#Moving onto the Directory
os.chdir(dir_name) 
dir_path = os.path.dirname(os.path.realpath(__file__))

x = 0
#Setting up the Pooling Limit to be 5 Images
pool_limit = 5
#Writing the Image 
for images in image_tag:
    try:
        #Getting the Source of the Image from the Server
        url_src = images["src"]
        #Getting the Status of the Image
        alt_data = images['alt']
        responce = requests.get(url_src)
        #If return anything
        if responce.status_code == 200:
            #Writing the Image onto the File in Binary
            if len(os.listdir(dir_path)) <= pool_limit:  
                with open("img."+str(x)+".jpg","wb") as f:
                    f.write(requests.get(url_src).content)
                    f.close()
                    x += 1

                #Writing the Title file
                with open(title_save_file,"a") as t:
                    t.write(alt_data+"\n")
                    t.close()

    except Exception as e:
        pass

    
    










