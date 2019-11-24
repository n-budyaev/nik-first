import time
#print('О чем напомнить?')
mes = str(input('О чем напомнить?'))
print('Через сколько минут?')
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(mes)
