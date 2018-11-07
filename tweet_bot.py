import tweepy as tp
import time
import os

#These Variables Contains our Twitter API Credentials
CONSUMER_API_KEY = "402wQf4M6ot5i1aM6Azfjb7oo"
CONSUMER_API_SEC = "ypeQp54kTESW2hLgpNzbRiFZafg4Gw00qYcmiQosGBM4q4YED6"
ACCESS_TOKEN = "1059616729213546497-xARRms7dQicurzDXGLwJSddLe0aQTI"
ACCESS_TOKEN_SEC = "E24ZgyiEXQozZntQ1WVbtxep0TcjiyMPBpJ8ZximOVPPz"

#Getting access into the Twiter API
auth = tp.OAuthHandler(consumer_key=CONSUMER_API_KEY, consumer_secret=CONSUMER_API_SEC)
auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SEC)
API_ACCESS = tp.API(auth)

#Changing the Directory to Access the Images
img_dir = "pictures"
os.chdir(img_dir)

current_dir = os.path.dirname(os.path.realpath(__file__))
title_dir_name = "titles"
title_save_file = "titles.txt"

# This Function will Return the Title Array
def titles_retuner(file_name):
	title_img = []
	with open(os.path.join(file_name),"r") as r:
		string = r.readlines()
		for n,data in enumerate(string):
			title_img.append(data.split("\n"))
	return title_img
title = titles_retuner(title_save_file)

# This will Run the Twitter API
for n,image in enumerate(os.listdir(current_dir)):
	try:
		#We are Uploading the Image with Unique Status
		API_ACCESS.update_with_media(image,status=title[n][0])
		time.sleep(3)
	except Exception as e:
		pass


