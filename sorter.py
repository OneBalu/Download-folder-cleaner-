import os, shutil
path = r"C:\Users\balaz\Downloads" #IDE A CÉLMAPPÁT KELL BERAKNI így: r"C:\Users\user\Downloads"

folder_names = ["Dokumentumok", "Média", "Torrent", "Rar", "Exe", "Egyéb"]
files_list = os.listdir(path)

file_group_documents = ['.docx', ".txt", ".pdf", ".pptx", ".xlsx", ".ppt" ]
file_group_media = [".jpg", ".png", ".mp4", ".wav", ".mp3", ".m4a"]
file_group_torrent = [".torrent"]
file_group_rar = [".rar", ".zip"]
file_group_exe = [".exe"]

os.listdir(path)

print("\n \n \n \n \nTakaritás kezdése... \n")

for f in folder_names:
    if os.path.exists(path + '/'+ f):
        print(f + " mappa létezik!")
    else:
        os.makedirs(path + "/" + f)
        print(f + " mappa létrehozva!")


for t in files_list:
    for doc in file_group_documents:
        if doc in t:
            shutil.move(path + "/" + t, path + "/Dokumentumok/")
    for med in file_group_media:
        if med in t:
            shutil.move(path + "/" + t, path + "/Média/")
    for torr in file_group_torrent:
        if torr in t:
            shutil.move(path + "/" + t, path + "/Torrent/")
    for rar in file_group_rar:
        if rar in t:
            shutil.move(path + "/" + t, path + "/Rar/")
    for exe in file_group_exe:
        if exe in t:
            shutil.move(path + "/" + t, path + "/Exe/")

            
for others in os.listdir(path):
    if others not in folder_names:
        shutil.move(path + "/" + others, path + "/Egyéb/")


print("\nTakarítás befejeződött! \n \n \n \n")

