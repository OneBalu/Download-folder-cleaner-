import os, shutil
path = r"C:\Users\balaz\Downloads" #IDE A CÉLMAPPÁT KELL BERAKNI így: r"C:\Users\user\Downloads"

folder_names = ["Dokumentumok", "Média", "Torrent", "Rar", "Exe", "Egyéb"]
files_list = os.listdir(path)

file_group_documents = ['.docx', ".txt", ".pdf", ".pptx", ".xlsx", ".ppt" ]
file_group_media = [".jpg", ".png", ".mp4", ".wav", ".mp3", ".m4a"]
file_group_torrent = [".torrent"]
file_group_rar = [".rar", ".zip"]
file_group_exe = [".exe"]
file_group_all = ['.docx', ".txt", ".pdf", ".pptx", ".xlsx", ".ppt",".jpg", ".png", ".mp4", ".wav", ".mp3", ".m4a", ".torrent", ".rar", ".zip", ".exe" ]
others_counter = 0
os.listdir(path)

print("\n \n \n \n \nTakaritás kezdése... \n")

for f in folder_names:
    if os.path.exists(path + '/'+ f):
        print(f + " mappa létezik!")
    else:
        os.makedirs(path + "/" + f)
        print(f + " mappa létrehozva!")


for t in files_list:
    if t in os.listdir(path) and \
        t in os.listdir(path + "/Dokumentumok/") or \
        t in os.listdir(path + "/Média/") or \
        t in os.listdir(path + "/Torrent/") or \
        t in os.listdir(path + "/Rar/") or \
        t in os.listdir(path + "/Exe/") or \
        t in os.listdir(path + "/Egyéb/"):
        print("duplikátum észlelve") 
        

    else:
        for doc in file_group_documents:
            if doc in t:
                shutil.move(path + "/" + t, path + r"/Dokumentumok/")
        for med in file_group_media:
            if med in t:
                shutil.move(path + "/" + t, path + r"/Média/")
        for torr in file_group_torrent:
            if torr in t:
                shutil.move(path + "/" + t, path + r"/Torrent/")
        for rar in file_group_rar:
            if rar in t:
                shutil.move(path + "/" + t, path + r"/Rar/")
        for exe in file_group_exe:
            if exe in t:
                shutil.move(path + "/" + t, path + r"/Exe/")

            
for others in os.listdir(path):
    if others in os.listdir(path) and \
        others in os.listdir(path + "/Dokumentumok/") or \
        others in os.listdir(path + "/Média/") or \
        others in os.listdir(path + "/Torrent/") or \
        others in os.listdir(path + "/Rar/") or \
        others in os.listdir(path + "/Exe/") or \
        others in os.listdir(path + "/Egyéb/"):
        print("duplikátum észlelve") 
    else:
        if others not in folder_names:
            shutil.move(path + "/" + others, path + r"/Egyéb/")

#print(others_counter, " darab duplikátum észlelve és törölve!")
print("\nTakarítás befejeződött! \n \n \n \n")

#ez egy komment
