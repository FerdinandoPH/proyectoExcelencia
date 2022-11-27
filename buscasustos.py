import os,getpass
for ruta, directorios, archivos in os.walk("C:\\Users\\"+getpass.getuser()):
    for archivo in archivos:
        if archivo=="susto.exe":
           print(ruta+"\\"+archivo)
print("no")
if os.path.exists("D:\\Users\\"):
    for ruta, directorios, archivos in os.walk("D:\\Users\\"+getpass.getuser()):
        for archivo in archivos:
            if archivo=="susto.exe":
                print(ruta+"\\"+archivo)
a=input("")