from rich import print

with open("./remarks.txt", "r", encoding="utf8") as f:
    data = f.read()

data = data.split("\n")
count = 0
for i, element in enumerate(data):
    # if "PRINCIPAL / HEAD TEACHER'S REMARKS" in element:
    #     print(data[i + 1])
    # if "Physics 0625" in element:
    #     count += 1
    #     print(f"{i = } -- {count = }")
    if "Mid Year Report   2021-22" in element:
        i += 139
        for j in range(0, 139):
            print(f"{data[j] = }")
        break
