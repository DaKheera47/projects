from pick import pick

data = [{'name': 'Zuha Aziz Khan', 'marks': 47}, {'name': 'Ranya Najeeb', 'marks': 42}, {'name': 'Maheen Tahir', 'marks': 55}, {'name': 'Varda Kahan', 'marks': 0}, {'name': 'Inayah Khan', 'marks': 54}, {'name': 'Ayesha Mariam', 'marks': 55}, {'name': 'Enayah Humera Aslam', 'marks': 37}, {
    'name': 'Hooria Nadeem', 'marks': 53}, {'name': 'Eman Umar', 'marks': 53}, {'name': 'Abeer Hassan Rana', 'marks': 44}, {'name': 'Mifrah Shahbaz', 'marks': 51}, {'name': 'Hiba Ayaz', 'marks': 38}, {'name': 'Labiqa Khan Burki', 'marks': 44}, {'name': 'Taishmina Ahmed', 'marks': 43}, {'name': 'Zymal Usman', 'marks': 45}]

names = [d['name'] for d in data]
# names = ['Alice', "Alina", "Ali", 'Bob', 'Charlie']
# search  through names

search = input("Search for a name: ").lower()

possibilities = []
for name in names:

    if name.lower().startswith(search):
        possibilities.append(name)

chosen = pick(possibilities, 'Pick a name')
print(names.index(chosen[0]))
