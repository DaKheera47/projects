import PyPDF2

from pathlib import Path
import requests

code = "41"

for i in range(16, 22):
    if i == 20:
        continue

    fileName = f"9702_s{i}_gt.pdf"
    link = f"https://papers.gceguide.com/A%20Levels/Physics%20(9702)/20{i}/{fileName}"

    file = Path(fileName)
    response = requests.get(link)
    file.write_bytes(response.content)


    with open(fileName, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        pageObj = reader.getPage(0)
        text = pageObj.extractText()


    text = text.split("\n")
    for j, item in enumerate(text):
        if f"component {code}" in item.lower():
            for k in range(0, 7):
                value = text[j + k]
                if k == 0:
                    print(f"{value} -- Year: {i}")
                elif k == 1:
                    print(f"Max Marks: {value}")
                elif k == 2:
                    print(f"A: {value}")
                elif k == 3:
                    print(f"B: {value}")
                elif k == 4:
                    print(f"C: {value}")
