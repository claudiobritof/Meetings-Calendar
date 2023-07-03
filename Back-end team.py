from datetime import time,datetime

x_gb_mon=[['19:40','21:00'],['21:40','23:30']]
x_bt_mon=[['07:00','08:00']]

bounds_gb_mon=['08:00','19:10']
bounds_bt_mon=['08:00','22:00']

time_def=30

print('-'*100)

def free_time(x, bounds, time):
    free = []
    b_start = datetime.strptime(bounds[0], "%H:%M")
    b_end = datetime.strptime(bounds[1], "%H:%M")
    start = datetime.strptime(x[0][0], "%H:%M")
    end = datetime.strptime(x[len(x) - 1][1], "%H:%M")
    min_start = (b_start - start).seconds / 60
    min_end = (b_end - end).seconds / 60
    if min_start >= float(time):
        if b_start < start:
            free.append([bounds[0], x[0][0]])
    for i in range(len(x) - 1):
        if ((datetime.strptime(x[i + 1][0], "%H:%M") - datetime.strptime(x[i][1], "%H:%M")).seconds / 60) >= float(
                time):
            free.append([x[i][1], x[i + 1][0]])
    if min_end >= float(time):
        if b_end > end:
            free.append([x[len(x) - 1][1], bounds[1]])
    return free

free_time(x_gb_mon,bounds_gb_mon,time_def)
free_time(x_bt_mon,bounds_bt_mon,time_def)
print(f'Free-time Brandão (monday): {free_time(x_gb_mon,bounds_gb_mon,time_def)}')
print(f'Free-time Trevelin (monday): {free_time(x_bt_mon,bounds_bt_mon,time_def)}')

def meeting_time(calendar1, calendar2, time):
    pres = []
    final = []
    for i in range(len(calendar1)):
        for j in range(len(calendar2)):
            if datetime.strptime(calendar1[i][1], "%H:%M") <= datetime.strptime(calendar2[j][1], "%H:%M"):
                if datetime.strptime(calendar1[i][0], "%H:%M") >= datetime.strptime(calendar2[j][0], "%H:%M"):
                    if ((datetime.strptime(calendar1[i][1], "%H:%M") - datetime.strptime(calendar1[i][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar1[i][0], calendar1[i][1]])
                else:
                    if ((datetime.strptime(calendar1[i][1], "%H:%M") - datetime.strptime(calendar2[j][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar2[j][0], calendar1[i][1]])
            else:
                if datetime.strptime(calendar1[i][0], "%H:%M") >= datetime.strptime(calendar2[j][0], "%H:%M"):
                    if ((datetime.strptime(calendar2[j][1], "%H:%M") - datetime.strptime(calendar1[i][0],
                                                                                         "%H:%M")).seconds / 60) >= float(
                            time):
                        pres.append([calendar1[i][0], calendar2[j][1]])
    for i in range(len(pres)):
        if datetime.strptime(pres[i][0], "%H:%M") < datetime.strptime(pres[i][1], "%H:%M"):
            final.append([pres[i][0], pres[i][1]])
    return final

print('-'*100)

meeting_time(free_time(x_gb_mon,bounds_gb_mon,time_def),free_time(x_bt_mon,bounds_bt_mon,time_def),time_def)

#Back-End Meeting Time:
print(f'Back-end meeting time (monday): {meeting_time(free_time(x_gb_mon,bounds_gb_mon,time_def),free_time(x_bt_mon,bounds_bt_mon,time_def),time_def)}')