import time,math
inicio=time.time()
while True:
    ahora=time.time()
    diff=math.floor(86400-(ahora-inicio))
    m, s = divmod(diff, 60)
    h, m = divmod(m, 60)
    print(f'{h:d}:{m:02d}:{s:02d}')
    time.sleep(1)
    