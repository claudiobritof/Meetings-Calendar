from datetime import time,datetime
from defs import free_time,meeting_time

x_bb_tue=[['14:00','16:00']]
x_cb_tue=[['09:00','18:00']]
x_gb_tue=[['19:10','20:00'],['21:40','23:30']]
x_bt_tue=[['19:10','23:30']]

bounds_bb_tue=['08:00', '22:00']
bounds_cb_tue=['09:00', '22:15']
bounds_gb_tue=['08:00', '18:40']
bounds_bt_tue=['08:00', '22:00']

time_def=30

print('='*100)
print('Free-time Front-end (tuesday): ')
free_time(x_bb_tue, bounds_bb_tue, time_def)
free_time(x_cb_tue, bounds_cb_tue, time_def)
print(f'Bouwman: {free_time(x_bb_tue, bounds_bb_tue, time_def)}')
print(f'Cláudio: {free_time(x_cb_tue, bounds_cb_tue, time_def)}')
print()
print('Free-time Back-end (tuesday): ')
free_time(x_gb_tue, bounds_gb_tue, time_def)
free_time(x_bt_tue, bounds_bt_tue, time_def)
print(f'Brandão: {free_time(x_gb_tue, bounds_gb_tue, time_def)}')
print(f'Trevelin: {free_time(x_bt_tue, bounds_bt_tue, time_def)}')

fronttue=meeting_time(free_time(x_bb_tue, bounds_bb_tue, time_def), free_time(x_cb_tue, bounds_cb_tue, time_def), time_def)
backtue=meeting_time(free_time(x_gb_tue, bounds_gb_tue, time_def), free_time(x_bt_tue, bounds_bt_tue, time_def), time_def)
senatue=meeting_time(meeting_time(free_time(x_bb_tue, bounds_bb_tue, time_def), free_time(x_cb_tue, bounds_cb_tue, time_def), time_def), meeting_time(free_time(x_gb_tue, bounds_gb_tue, time_def), free_time(x_bt_tue, bounds_bt_tue, time_def), time_def), time_def)