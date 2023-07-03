from datetime import time,datetime
from defs import free_time,meeting_time

x_bb_mon=[['16:00','19:00'],['22:00','23:00']]
x_cb_mon=[['09:00','16:00'],['22:15','23:59']]
x_gb_mon=[['19:40','21:00'],['21:40','23:30']]
x_bt_mon=[['07:00','08:00']]

bounds_bb_mon=['08:00','22:00']
bounds_cb_mon=['09:00','22:15']
bounds_gb_mon=['08:00','19:10']
bounds_bt_mon=['08:00','22:00']

time_def=30

print('='*100)
print('Free-time Front-end (monday): ')
free_time(x_bb_mon,bounds_bb_mon,time_def)
free_time(x_cb_mon,bounds_cb_mon,time_def)
print(f'Bouwman: {free_time(x_bb_mon,bounds_bb_mon,time_def)}')
print(f'Cláudio: {free_time(x_cb_mon,bounds_cb_mon,time_def)}')
print()
print('Free-time Back-end (monday): ')
free_time(x_gb_mon,bounds_gb_mon,time_def)
free_time(x_bt_mon,bounds_bt_mon,time_def)
print(f'Brandão: {free_time(x_gb_mon,bounds_gb_mon,time_def)}')
print(f'Trevelin: {free_time(x_bt_mon,bounds_bt_mon,time_def)}')

frontmon=meeting_time(free_time(x_bb_mon,bounds_bb_mon,time_def),free_time(x_cb_mon,bounds_cb_mon,time_def),time_def)
backmon=meeting_time(free_time(x_gb_mon,bounds_gb_mon,time_def),free_time(x_bt_mon,bounds_bt_mon,time_def),time_def)
senamon=meeting_time(meeting_time(free_time(x_bb_mon,bounds_bb_mon,time_def),free_time(x_cb_mon,bounds_cb_mon,time_def),time_def),meeting_time(free_time(x_gb_mon,bounds_gb_mon,time_def),free_time(x_bt_mon,bounds_bt_mon,time_def),time_def),time_def)