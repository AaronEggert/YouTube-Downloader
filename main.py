import os
import subprocess
from pytube import YouTube, Playlist


videos = []


def credits():
    print("     ┌─────────────────────────────────────────────────────────────────────┐")
    print("     │                   Thank you for using my Tool!!                     │")
    print("     │                  (👉ﾟヮﾟ)👉 Github: @AaronEggert                    │")
    print("     │   Source Code: https://github.com/AaronEggert/YouTube-Downloader    │")
    print("     └─────────────────────────────────────────────────────────────────────┘")


def check():
    print("----- Checking: -----")
    for video in videos:
        mp4 = None
        if os.path.exists(video["path"]):
            print(f"\u001b[32mJ {video['path']}\u001b[0m")
            mp4 = True
        else:
            print(f"\u001b[31mX {video['path']}\u001b[0m")
            mp4 = False
        if video["convert"]:
            if os.path.exists(video["mp3_path"]):
                print(f"\u001b[32mJ {video['mp3_path']}\u001b[0m")
                if mp4:
                    os.remove(video["path"])
                    print(f"\u001b[32mDeleted {video['path']}\u001b[0m")
            else:
                print(f"\u001b[31mX {video['mp3_path']}\u001b[0m")
    credits()
    exit(0)


def convert():
    print("----- Converting: -----")
    for video in videos:
        if video["convert"]:
            video["mp3_path"] = video["path"][0:-1] + '3'
            p = subprocess.Popen(f'ffmpeg -i "' + video["path"] + '" "' + video["mp3_path"] + '"')
            p.wait()


def download(path):
    print("----- Downloading: -----")
    for video in videos:
        print(f"\u001b[33mDownloading {video['v'].title}...\u001b[0m")
        v_path = video["v"].streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(output_path=path)
        video["path"] = v_path
    convert()
    check()


def add_to_list(link):
    try:
        v = YouTube(link)
        p = None
    except Exception:
        v = None
        try:
            p = Playlist(link)
        except Exception:
            return False
    
    if v:
        i = input('Convert to mp3? y/N: ')
        if i == "y" or i == "Y":
            con = True
        else:
            con = False
        videos.append({"v": v, "convert": con})
    if p:
        print("> " + p.title + " " + p.owner)
        print("> " + str(p.length) + " videos")
        inp = True
        while inp:
            i = input(">exit with 'ext'; How much to Add? Start by 0; x-y: ")
            if i == "ext":
                return True
            c = 0
            for j in i:
                if j == "-":
                    break
                c += 1
            try:
                first = int(i[0:c])
                second = int(i[c+1:len(i)])
                if 0 <= first < second <= p.length:
                    print(first, "to", second)
                    i = input("Correct? y/N: ")
                    if i == "y" or i == "Y":
                        inp = False
                        vids_to_add = p[first:second]
                        i = input("Convert all to mp3? y/N: ")
                        if i == "y":
                            con = True
                        else:
                            con = False
                        for i in vids_to_add:
                            temp_v = YouTube(i)
                            videos.append({"v": temp_v, "convert": con})

            except Exception as e:
                print(e)
                return False, e


def interface():
    a = True
    while a:
        os.system('cls')
        #print(converts)
        p = '┌─── Title ───────────────────────────────────────┬─── Video URL ─────────────────────────────┬─ Convert ─┐\n'
        c = 0
        for video in videos:
            #print(video)
            title = video["v"].title
            print(title)
            # 39 - 5
            url = video["v"].watch_url
            if c < 10:
                form_c = f"  {c}"
            elif 10 <= c < 100:
                form_c = f" {c}"
            else:
                form_c = f"{c}"
            if len(title) < 43:
                form_title = title
                l = 44 - len(title)
                for i in range(l):
                    form_title += " "
            if len(title) > 43:
                form_title = title[0:42] + ".."
            form_url = url
            l = 42 - len(url)
            for i in range(l):
                form_url += " "
            if video["convert"]:
                form_con = " True      "
            else:
                form_con = " False     "

            p += f'│{form_c}. {form_title}│ {form_url}│{form_con}│\n'
            c += 1
        p += '└─────────────────────────────────────────────────┴───────────────────────────────────────────┴───────────┘\n'
        os.system('cls')
        credits()
        print("")
        print(p)
        print("1. Add Video or Playlist")
        print("2. Delete from list")
        print("3. Start Donwload")
        print("4. Exit\n")
        i = input('Choose: ')
        if i == "1":
            v_in = input("Video or Playlist Url: ")
            add_to_list(v_in)
        elif i == "2":
            del_in = input("Indexnumber of Item: ")
            try:
                num = int(del_in)
                videos.pop(num)
            except Exception as e:
                print(e)
            pass
        elif i == "3":
            path = input(f"Enter download Path: ({os.path.dirname(os.path.realpath(__file__))}) ")
            if not path:
                path = os.path.dirname(os.path.realpath(__file__))
            print(path)
            download(path)
        elif i == "4":
            exit(1)

if __name__ == '__main__':
    interface()
