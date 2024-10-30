import requests
print("[1] Install")
print("[2] Info")
print("[3] Exit")
choice = input("What do ya think? (case sensitive, ex: Install) ")
if (choice == "Install"):
    print("Alright! We're installing...")
    url = 'https://github.com/wish13yt/BitViewOS/blob/main/BitviewOS.py?raw=true'


    response = requests.get(url)
    file_Path = 'BitviewOS.py'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('Installed!')
    else:
        print('Failed to download file')
if (choice == "Info"):
    print("Setup 1.0")
    print("10/30/2024")
    print("Idea by @thatgaminguser on PikiDiary")
    print("Code by @wish on PikiDiary")
if (choice == "Exit"):
    raise SystemExit