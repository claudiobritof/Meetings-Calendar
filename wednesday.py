from datetime import time,datetime
from defs import free_time,meeting_time

x_bb_wed=[['11:00', '13:00'], ['15:00', '19:00']]
x_cb_wed=[['09:00', '18:00']]
x_gb_wed=[['19:40', '21:00'], ['21:40', '23:30']]
x_bt_wed=[['07:00', '08:00']]

bounds_bb_wed=['08:00', '22:00']
bounds_cb_wed=['09:00', '22:00']
bounds_gb_wed=['08:00', '19:10']
bounds_bt_wed=['08:00', '22:00']

time_def=30

print('='*100)
print('Free-time Front-end (wednesday): ')
free_time(x_bb_wed, bounds_bb_wed, time_def)
free_time(x_cb_wed, bounds_cb_wed, time_def)
print(f'Bouwman: {free_time(x_bb_wed, bounds_bb_wed, time_def)}')
print(f'Cláudio: {free_time(x_cb_wed, bounds_cb_wed, time_def)}')
print()
print('Free-time Back-end (wednesday): ')
free_time(x_gb_wed, bounds_gb_wed, time_def)
free_time(x_bt_wed, bounds_bt_wed, time_def)
print(f'Brandão: {free_time(x_gb_wed, bounds_gb_wed, time_def)}')
print(f'Trevelin: {free_time(x_bt_wed, bounds_bt_wed, time_def)}')

frontwed=meeting_time(free_time(x_bb_wed, bounds_bb_wed, time_def), free_time(x_cb_wed, bounds_cb_wed, time_def), time_def)
backwed=meeting_time(free_time(x_gb_wed, bounds_gb_wed, time_def), free_time(x_bt_wed, bounds_bt_wed, time_def), time_def)
senawed=meeting_time(meeting_time(free_time(x_bb_wed, bounds_bb_wed, time_def), free_time(x_cb_wed, bounds_cb_wed, time_def), time_def), meeting_time(free_time(x_gb_wed, bounds_gb_wed, time_def), free_time(x_bt_wed, bounds_bt_wed, time_def), time_def), time_def)