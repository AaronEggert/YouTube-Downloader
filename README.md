# YouTube-Downloader

## Features
- Download Videos
- Download Playlist
  - Specific videos from playlist
- Convert Videos automaticly in .mp3

## Instalation
1. Install Required packages:
```
$ pip install -r requirements.txt
```
2. Install [FFmpeg](https://ffmpeg.org/download.html) (Used to convert .mp4 -> .mp3)
    - ffmpeg.exe has to be in system Enviorments path
         - [tutorial for windows](https://www.computerhope.com/issues/ch000549.htm)
         - linux user know ;)

## How to use
1. Start the script
2. Add videos and Playlists
    - If you want to add a playlist you can choose how much videos to add
    - Also you can decide if you want to convert the videos directly into .mp3 after downloading (only if FFmpeg is installed)  
 3. You can remove a video from the queue when you wrongly added it
 4. Start Download
    - Now you can enter a download path or press enter to download it in the filder where the script is
    - Now the files where downloaded, converted and checked
    - at the end you can see if the files exists if they are green in the console
    - if there is a path red means that something gone wrong and file didnt exists
