#Programa para pasar archivos a una cadena en base64
import base64,pyperclip
archivo=input("Ingrese el nombre del archivo: ")
with open(archivo,"rb") as f:
    s=f.read()
    pyperclip.copy(str(base64.b64encode(s)))
    print("ya")
    f.close()