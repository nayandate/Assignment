#An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds #(which their sensor system records) into a more #human-readable format of hours, minutes, and seconds.


duration=int(input("total event duration  in seconds:"))
hours=duration//3600
rem= duration%3600
min=rem//60
sec=rem%60
print("Hours:{},Min:{},Sec:{}".format(hours,min,sec))
