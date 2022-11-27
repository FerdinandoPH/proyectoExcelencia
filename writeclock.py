import time,getpass
usuario=getpass.getuser()
with open("C:\\Users\\"+usuario+"\\Documents\\ransomdetalles.txt","w") as f:
    f.truncate()
    f.write(str(time.time()))