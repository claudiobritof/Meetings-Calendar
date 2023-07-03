from datetime import time,datetime
from defs import free_time,meeting_time

x_bb_thu=[['15:00', '19:00']]
x_cb_thu=[['09:00', '18:00'], ['20:00', '21:00']]
x_gb_thu=[['18:10', '20:00'], ['20:40', '23:00']]
x_bt_thu=[['07:00', '08:00']]

bounds_bb_thu=['08:00', '22:00']
bounds_cb_thu=['09:00', '21:00']
bounds_gb_thu=['08:00', '17:40']
bounds_bt_thu=['08:00', '22:00']

time_def=30

print('='*100)
print('Free-time Front-end (thursday): ')
free_time(x_bb_thu, bounds_bb_thu, time_def)
free_time(x_cb_thu, bounds_cb_thu, time_def)
print(f'Bouwman: {free_time(x_bb_thu, bounds_bb_thu, time_def)}')
print(f'Cláudio: {free_time(x_cb_thu, bounds_cb_thu, time_def)}')
print()
print('Free-time Back-end (thursday): ')
free_time(x_gb_thu, bounds_gb_thu, time_def)
free_time(x_bt_thu, bounds_bt_thu, time_def)
print(f'Brandão: {free_time(x_gb_thu, bounds_gb_thu, time_def)}')
print(f'Trevelin: {free_time(x_bt_thu, bounds_bt_thu, time_def)}')

frontthu=meeting_time(free_time(x_bb_thu, bounds_bb_thu, time_def), free_time(x_cb_thu, bounds_cb_thu, time_def), time_def)
backthu=meeting_time(free_time(x_gb_thu, bounds_gb_thu, time_def), free_time(x_bt_thu, bounds_bt_thu, time_def), time_def)
senathu=meeting_time(meeting_time(free_time(x_bb_thu, bounds_bb_thu, time_def), free_time(x_cb_thu, bounds_cb_thu, time_def), time_def), meeting_time(free_time(x_gb_thu, bounds_gb_thu, time_def), free_time(x_bt_thu, bounds_bt_thu, time_def), time_def), time_def)