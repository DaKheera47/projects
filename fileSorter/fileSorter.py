import os
import shutil

outputFolder = os.path.abspath("./outputFolder")

typesOfFiles = {
    "images": {
        "extensions": (".jpeg", ".jpg", ".png", ".gif", ".ico"),
        "outputFolder": f"{outputFolder}/images"
    },
    "pdfs": {
        "extensions": (".pdf"),
        "outputFolder": f"{outputFolder}/pdfs"
    },
    "inpages": {
        "extensions": (".inp", "B01"),
        "outputFolder": f"{outputFolder}/inpages"
    },
    "zips": {
        "extensions": (".zip", ".rar"),
        "outputFolder": f"{outputFolder}/compressed"
    },
    "exes": {
        "extensions": (".exe", ".msi"),
        "outputFolder": f"{outputFolder}/executables"
    },
    "audios": {
        "extensions": (".mp3"),
        "outputFolder": f"{outputFolder}/audios"
    },
    "videos": {
        "extensions": (".mp4", ".mkv"),
        "outputFolder": f"{outputFolder}/videos"
    },
    "figmas": {
        "extensions": (".fig"),
        "outputFolder": f"{outputFolder}/figmaFiles"
    },
    "documents": {
        "extensions": (".doc", ".docx", ".xlsx", ".xls", ".txt"),
        "outputFolder": f"{outputFolder}/documents"
    },
    "misc": {
        "extensions": (".*"),
        "outputFolder": f"{outputFolder}/misc"
    },
}

for folder in typesOfFiles:
    try:
        os.makedirs(typesOfFiles[folder]["outputFolder"])
        print(folder)
    except FileExistsError:
        pass


def matchFile(file):
    ext = os.path.splitext(file)[-1].lower()
    print(file)

    isSorted = False

    for typ in typesOfFiles:
        if ext in typesOfFiles[typ]["extensions"]:
            shutil.move(file, typesOfFiles[typ]["outputFolder"])
            isSorted = True

    if isSorted == False:
        shutil.move(file, f"{outputFolder}/misc")


# allFiles = os.listdir()
# for file in allFiles:
#     if os.path.isfile(file):
#         if file != "fileSorter.py":
#             # print(os.path.abspath(file))
#             matchFile(os.path.abspath(file))

for dirpath, dirnames, filenames in os.walk("."):
    if "outputFolder" in dirnames:
        dirnames.remove("outputFolder")
    for filename in [f for f in filenames]:
        print(filename)

        file = os.path.abspath(os.path.join(dirpath, filename))
        if filename != "fileSorter.py":
            try:
                matchFile(file)
            except shutil.Error:
                print("err")



for folder in list(os.walk("."))[1:]:
    if not folder[2]:
        print(folder)
        os.rmdir(folder[0])
