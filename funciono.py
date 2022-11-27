if __name__ == '__main__':
    import ctypes
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if is_admin():
        print("BIEEEN")
    else:
        print("Ohhhh")
    a=input("")