import requests
print("[1] Update")
choice = input("What do ya say? (case-sensetive, ex: Update) ")
if (choice == "Update"):
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