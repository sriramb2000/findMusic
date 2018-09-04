#! python3
from apiclient.discovery import build
import os
import webbrowser
import sys
import random
from dotenv import load_dotenv

#load env vars
load_dotenv()

#create youtube instance
DEVELOPER_KEY = os.getenv("DEVELOPER_KEY")
youtube = build('youtube','v3', developerKey=DEVELOPER_KEY)

#decide whether to randomize choice
numResult = 0
if(sys.argv[1] <= 1):
    numResult = 1;
else:
    numResult = sys.argv[1]
#capping randomness
numResult %= 101

#build search string
search = ""
for x in range(2, len(sys.argv)):
    search += sys.argv[x] + " "

#query results
results = youtube.search().list(
    part='snippet',
    maxResults=numResult,
    q=search,
    type='playlist'
).execute()
results = results['items']

if(numResult == 1):
    chosenPlaylist = results[0]['id']['playlistId']
else:
    #choose random playlist from results
    chosenPlaylist = results[random.randint(0,len(results))]['id']['playlistId']

#get starting video
playlistData = youtube.playlistItems().list(
    part='contentDetails',
    maxResults=1,
    playlistId=chosenPlaylist
).execute()

#open playlist
webbrowser.open_new_tab('https://www.youtube.com/watch?v='+playlistData['items'][0]['contentDetails']['videoId']+'&list='+chosenPlaylist)
