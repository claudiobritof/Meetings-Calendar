from datetime import time,datetime
from defs import free_time,meeting_time

x_bb_fri=[['14:00', '16:00']]
x_cb_fri=[['08:00', '16:00']]
x_gb_fri=[['19:40', '21:00']]
x_bt_fri=[['21:40', '22:30']]

bounds_bb_fri=['08:00', '22:00']
bounds_cb_fri=['09:00', '22:00']
bounds_gb_fri=['08:00', '19:10']
bounds_bt_fri=['08:00', '22:00']

time_def=30

print('='*100)
print('Free-time Front-end (friday): ')
free_time(x_bb_fri, bounds_bb_fri, time_def)
free_time(x_cb_fri, bounds_cb_fri, time_def)
print(f'Bouwman: {free_time(x_bb_fri, bounds_bb_fri, time_def)}')
print(f'Cláudio: {free_time(x_cb_fri, bounds_cb_fri, time_def)}')
print()
print('Free-time Back-end (friday): ')
free_time(x_gb_fri, bounds_gb_fri, time_def)
free_time(x_bt_fri, bounds_bt_fri, time_def)
print(f'Brandão: {free_time(x_gb_fri, bounds_gb_fri, time_def)}')
print(f'Trevelin: {free_time(x_bt_fri, bounds_bt_fri, time_def)}')

frontfri=meeting_time(free_time(x_bb_fri, bounds_bb_fri, time_def), free_time(x_cb_fri, bounds_cb_fri, time_def), time_def)
backfri=meeting_time(free_time(x_gb_fri, bounds_gb_fri, time_def), free_time(x_bt_fri, bounds_bt_fri, time_def), time_def)
senafri=meeting_time(meeting_time(free_time(x_bb_fri, bounds_bb_fri, time_def), free_time(x_cb_fri, bounds_cb_fri, time_def), time_def), meeting_time(free_time(x_gb_fri, bounds_gb_fri, time_def), free_time(x_bt_fri, bounds_bt_fri, time_def), time_def), time_def)