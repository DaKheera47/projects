import pyautogui as pag
import time
import re

className = 9
discription = " "

# names = open("name.txt", "r")
fileUrls = open("fileUrl.txt", "r")
# names = list(name.strip() for name in names)

i = 1

pag.hotkey("alt", "tab")
pag.PAUSE = 0.01
for url in fileUrls:
    # get just the filename from url string
    # print(url)
    url = url.split()[0]
    
    # for name in names:
        # if name == url.split("/")[5].split()[0][:-9]:
    typeName = f"paper{i}"
    print(i, url)
    pag.write(f'http -f POST localhost:8080/admin/createNewListening class={className} type="{typeName}" discription="Question 3" fileUrl={url} url="{url.split("/")[5].split()[0][:-9]}" title=" "\n', interval=0.01)
    i += 1
    
    
    time.sleep(3)
