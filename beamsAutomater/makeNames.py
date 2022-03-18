import pyautogui as pag
import time
from collections import OrderedDict
from rich.console import Console
console = Console()

codes = [
    {
        "name": "Mathematics",
        "code": "0580"
    },
    {
        "name": "Add Maths",
        "code": "4037"
    },
    {
        "name": "Urdu",
        "code": "0539"
    },
    {
        "name": "Pakistan Studies",
        "code": "0488"
    },
    {
        "name": "Islamiat",
        "code": "0493"
    },
    {
        "name": "English",
        "code": "0500"
    },
    {
        "name": "Chemistry",
        "code": "0620"
    },
    {
        "name": "Physics",
        "code": "0625"
    },
    {
        "name": "Computer Science",
        "code": "0478"
    },
    {
        "name": "Business Studies",
        "code": "0450"
    },
    {
        "name": "Accounting",
        "code": "0452"
    },
    {
        "name": "GP",
        "code": "0457"
    },
    {
        "name": "English Literature",
        "code": "0475"
    },
    {
        "name": "English As A Second Language",
        "code": "0510"
    },
    {
        "name": "Sociology",
        "code": "0495"
    },
    {
        "name": "Arts and Design",
        "code": "0400"
    },
    {
        "name": "Economics",
        "code": "0455"
    },
]

data = [
    {
        "studentName": "Naveera Seerat",
        "id": "115831",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Business Studies",
            "Computer Science",
            "GP",
            "Economics",
        ]
    },
    {
        "studentName": "Yashfa Baloch",
        "id": "141513",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Computer Science",
            "Physics",
            "Chemistry",
            "GP",
            "Sociology",
        ]
    },
    {
        "studentName": "Abroo Sajid Kiani",
        "id": "161259",
        "compulsory": [
            "Mathematics",
            "English",
        ],
        "optional": [
            "Computer Science",
            "Physics",
            "Chemistry",
            "GP",
            "Sociology",
        ]
    },
    {
        "studentName": "Maira Mustafa",
        "id": "169406",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Arts and Design",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Manhal Fatima",
        "id": "176650",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Business Studies",
            "Accounting",
            "Economics",
            "English Literature",
        ]
    },
    {
        "studentName": "Amna Noor",
        "id": "176652",
        "compulsory": [
            "Mathematics",
            "English As A Second Language",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Eshaal Zeeshan",
        "id": "178387",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Sociology",
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science"
        ]
    },
    {
        "studentName": "Masjah Aziz",
        "id": "204354",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Zahra Masud Khan",
        "id": "221403",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "",
        ]
    },
    {
        "studentName": "Aymen Shahzad",
        "id": "235935",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Arts and Design",
            "Business Studies",
            "Accounting",
            "Economics",
        ]
    },
    {
        "studentName": "Maria Faisal",
        "id": "2320000212224",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Economics",
            "Business Studies",
            "Computer Science",
        ]
    },
    {
        "studentName": "Nayab Malik",
        "id": "3230000246139",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Business Studies",
            "Computer Science",
            "Economics",
        ]
    },
    {
        "studentName": "Hiba Ishtiaq",
        "id": "3260000246076",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Sociology",
            "Business Studies",
            "Economics",
            "Accounting",
        ]
    },
    {
        "studentName": "Alyesha Asif Qureshi",
        "id": "3320000242148",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Abeeha Fatima Mashhadi",
        "id": "3350000247053",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Rumaisa Sajid",
        "id": "6350000221983",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Ayesha Fatima",
        "id": "6820000223025",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "GP",
            "Physics",
            "Chemistry",
            "Computer Science",
        ]
    },
    {
        "studentName": "Hamnah Afraz",
        "id": "232408",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Economics",
            "Business Studies",
            "Arts and Design",
            "GP",
        ]
    },
    {
        "studentName": "Sameen Aftab",
        "id": "210798",
        "compulsory": [
            "Mathematics",
            "English",
            "Islamiat",
        ],
        "optional": [
            "Economics",
            "Business Studies",
            "GP",
            "Accounting",
        ]
    },
    {
        "studentName": "Minal Kashif",
        "id": "254059",
        "compulsory": [
            "Mathematics",
            "English",
            "Urdu",
            "Pakistan Studies",
            "Islamiat",
        ],
        "optional": [
            "Accounting",
            "Chemistry",
            "Physics",
        ]
    },
]

# https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
data = sorted(data, key=lambda x: x["studentName"])

time.sleep(3)
pag.PAUSE = 0.1

console.rule("[green on black]Number of subjects per student")
for student in data:
    counter = 0
    counter += len(student["compulsory"])
    counter += len(student["optional"])
    if counter <= 8:
        console.print(f'{student["studentName"]} - [red on black] {counter} Subjects')
    else:
        console.print(f'{student["studentName"]} - [green on black] {counter} Subjects')


# for i, student in enumerate(data, start=1):
    # pag.write(student["studentName"])
    # pag.write("X Silver")
    # pag.press("down")
