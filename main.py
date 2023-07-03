import defs
import monday, tuesday, wednesday, thursday, friday
from datetime import time,datetime

print()
print()
print()
print('MEETINGS CALENDAR')
print('='*100)
print('Daily Schedules (GMT+0 Time Zone)\n')

#Monday

print('MONDAY Meeting Time')
#Front-End Meeting Time:
print(f'Front-end: {monday.frontmon}')
#Back-End Meeting Time:
print(f'Back-end: {monday.backmon}')
#SENA Meeting Time (all):
print(f'SENA: {monday.senamon}')
print('-'*70)

#Tuesday

print('TUESDAY Meeting Time')
#Front-End Meeting Time:
print(f'Front-end: {tuesday.fronttue}')
#Back-End Meeting Time:
print(f'Back-end: {tuesday.backtue}')
#SENA Meeting Time (all):
print(f'SENA: {tuesday.senatue}')
print('-'*70)

#Wednesday

print('WEDNESDAY Meeting Time')
#Front-End Meeting Time:
print(f'Front-end: {wednesday.frontwed}')
#Back-End Meeting Time:
print(f'Back-end: {wednesday.backwed}')
#SENA Meeting Time (all):
print(f'SENA: {wednesday.senawed}')
print('-'*70)

#Thursday

print('THURSDAY Meeting Time')
#Front-End Meeting Time:
print(f'Front-end: {thursday.frontthu}')
#Back-End Meeting Time:
print(f'Back-end: {thursday.backthu}')
#SENA Meeting Time (all):
print(f'SENA: {thursday.senathu}')
print('-'*70)

#Friday

print('FRIDAY Meeting Time')
#Front-End Meeting Time:
print(f'Front-end: {friday.frontfri}')
#Back-End Meeting Time:
print(f'Back-end: {friday.backfri}')
#SENA Meeting Time (all):
print(f'SENA: {friday.senafri}')

#Duration of the meeting (minutes)

meeting_duration=30

print('='*100)
print()