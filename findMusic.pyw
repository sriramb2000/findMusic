#! python3
from apiclient.discovery import build
import webbrowser
import sys
import random

#create youtube instance
DEVELOPER_KEY = "AIzaSyAKoVaVByj-jH2cZLCcrNfvckdsesX0Wzw"
youtube = build('youtube','v3', developerKey=DEVELOPER_KEY)

#decide whether to randomize choice
numResult = 5
if(sys.argv[1] == "0"):
    numResult = 1;

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

playlistData = youtube.playlistItems().list(
    part='contentDetails',
    maxResults=1,
    playlistId=chosenPlaylist
).execute()

#open playlist
webbrowser.open_new_tab('https://www.youtube.com/watch?v='+playlistData['items'][0]['contentDetails']['videoId']+'&list='+chosenPlaylist)
