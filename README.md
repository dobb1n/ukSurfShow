# Auto podcast summariser

this project monitors a podcast rss feed, checking it daily for new episodes. it works out whether an episode is new by parsing the rss feed and comparing the episode names to those it has already seen. if an episode has not been seen before, the cloud function downloads it and sticks it in a GCS bucket. 

when a new file lands in the bucket, another function sends the audio to the speech to text api. this transcribes the audio into a text file which goes into a different folder. it then deletes the mp3 file. 

when a new transcript lands in the transcripts folder, another cloud function picks it up, reads the text, and summarises the content - saving its results in firestore, which can then be accessed through a next.js web app. 

## cf1 - episode checker
this is partly done. currently just grabs a specific episode

## cf2 - send to speech to text api
manual

## cf3 - analysis
not started

## fe portal
not started
