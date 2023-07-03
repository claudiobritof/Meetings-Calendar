from datetime import time,datetime

x_bb_mon=[['16:00','19:00'],['22:00','23:00']]
x_cb_mon=[['09:00','16:00'],['22:15','23:59']]

bounds_bb_mon=['08:00','22:00']
bounds_cb_mon=['09:00','22:15']

time_def=30

print('-'*100)

def free_time(x, bounds, time):
    new = []
    b_start = datetime.strptime(bounds[0], "%H:%M")
    b_end = datetime.strptime(bounds[1], "%H:%M")
    start = datetime.strptime(x[0][0], "%H:%M")
    end = datetime.strptime(x[len(x) - 1][1], "%H:%M")
    min_start = (b_start - start).seconds / 60
    min_end = (b_end - end).seconds / 60
    if min_start >= float(time):
        if b_start < start:
            new.append([bounds[0], x[0][0]])
    for i in range(len(x) - 1):
        if ((datetime.strptime(x[i + 1][0], "%H:%M") - datetime.strptime(x[i][1], "%H:%M")).seconds / 60) >= float(
                time):
            new.append([x[i][1], x[i + 1][0]])
    if min_end >= float(time):
        if b_end > end:
            new.append([x[len(x) - 1][1], bounds[1]])
    return new

free_time(x_bb_mon,bounds_bb_mon,time_def)
free_time(x_cb_mon,bounds_cb_mon,time_def)
print(f'Free-time Bouwman (monday): {free_time(x_bb_mon,bounds_bb_mon,time_def)}')
print(f'Free-time Cláudio (monday): {free_time(x_cb_mon,bounds_cb_mon,time_def)}')


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

#Front-End Meeting Time:
print(f'Front-End Meeting Time (monday): {meeting_time(free_time(x_bb_mon,bounds_bb_mon,time_def),free_time(x_cb_mon,bounds_cb_mon,time_def),time_def)}')

