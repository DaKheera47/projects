results = [{'name': 'Sambahain Sohail', 'grade': '5'}, {'name': 'Aaiza Ahmed', 'grade': '5'}, {'name': 'Hafsa Zafar', 'grade': '5'}, {'name': 'Syeda Emaan Zahra', 'grade': '5'}, {'name': 'Aisha Tariq', 'grade': '5'}, {'name': 'Hadia Akram', 'grade': '5'}, {'name': 'Emaan Ejaz', 'grade': '5'}, {'name': 'Abeera Farhan Zaidi', 'grade': '5'}, {'name': 'Iqra Zafar', 'grade': '5'}, {
    'name': 'Maheen Mazhar', 'grade': '5'}, {'name': 'Dua Nadeem', 'grade': '5'}, {'name': 'Schiza Zaheer', 'grade': '5'}, {'name': 'Hanna Ahmad Khan', 'grade': '5'}, {'name': 'Isra Abrar', 'grade': '5'}, {'name': 'Manaal Kashif', 'grade': '5'}, {'name': 'Syeda Aleena Shahid', 'grade': '5'}, {'name': 'Meshaim Ali Khan', 'grade': '5'}, {'name': 'Natalia Ahmad', 'grade': '5'}, {'name': 'Laiba Taimur', 'grade': '5'}]

noogrades = [{'name': 'Sambahain Sohail', 'grade': 'A'}, {'name': 'Aaiza Ahmed', 'grade': 'A*'}, {'name': 'Hafsa Zafar', 'grade': 'B'}, {'name': 'Syeda Emaan Zahra', 
'grade': 'A*'}, {'name': 'Aisha Tariq', 'grade': 'A'}, {'name': 'Hadia Akram', 'grade': 'A'}, {'name': 'Emaan Ejaz', 'grade': 'B'}, {'name': 'Abeera Farhan Zaidi', 'grade': 'A*'}, {'name': 'Iqra Zafar', 'grade': 'A'}, {'name': 'Maheen Mazhar', 'grade': 'A'}, {'name': 'Dua Nadeem', 'grade': 'B'}, {'name': 'Schiza Zaheer', 'grade': 'A'}, {'name': 'Hanna Ahmad Khan', 'grade': 'A*'}, {'name': 'Isra Abrar', 'grade': ' '}, {'name': 'Manaal Kashif', 'grade': 'A'}, 
{'name': 'Syeda Aleena Shahid', 'grade': 'A'}, {'name': 'Meshaim Ali Khan', 'grade': 'B'}, {'name': 'Natalia Ahmad', 'grade': 'A*'}, {'name': 'Laiba Taimur', 'grade': 'A'}]
# loop over dictionary
import time
import pyautogui as pag
time.sleep(2)
for i in noogrades:
    name = i['name']
    grade = i['grade']

    pag.typewrite(name)
    pag.press("tab")
    pag.typewrite(grade)
    pag.press(["enter"])

# print(results)
# for i in results:
#     name = i['name']
#     inp = input(f"{name}: ").upper()
#     if inp == "S":
#         i['grade'] = "A*"
#     else:
#         i['grade'] = inp
#     # print(f"{i['name']}: {i['grade']}")

# print(results)