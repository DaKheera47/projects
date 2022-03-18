import os

path = r'C:\Users\dakonwindows\Downloads\q3\\'

for file in os.listdir(path):
    # vibe = file.replace(".EX1.", "-")
    
    # lower all 
    vibe = file.lower()
    
    noExt = os.path.splitext(vibe)[0]
    
    out = ''.join([i for i in noExt if not i.isdigit()]).replace(" ", "")
    
    print(out + os.path.splitext(vibe)[1])
    os.rename(path + file, path + out + os.path.splitext(vibe)[1])

# then = os.listdir(path)
# print(then)