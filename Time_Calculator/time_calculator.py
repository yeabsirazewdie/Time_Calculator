def add_time(start, duration,day=' '):
  
  #get the day argument
  day=day.lower()
  day=day.capitalize()
  weekDays=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
  
  #get the start argument and alter it accordingly
  timestampStart=start.split(' ')
  timeStart=timestampStart[0].split(':')
  if(timestampStart[1]=='PM'):
    timeStart[0]=str(int(timeStart[0])+12)
  minuteStart=[int(timeStart[0])*60,int(timeStart[1])]
  
  #get the duration argument and alter it accordingly
  timestampDuration=duration.split(' ')
  timeDuration=timestampDuration[0].split(':')
  minuteDuration=[int(timeDuration[0])*60,int(timeDuration[1])]
  
  #get the total minutes
  total=minuteStart[0]+minuteStart[1]+minuteDuration[0]+minuteDuration[1]

  #decide on whether the day has changed (and PM to AM)
  leftMins=total%1440
  days=(total-leftMins)/1440
  
  if(leftMins<=720):
    temp=leftMins%60
    hours=(leftMins-temp)/60
    if(hours==0.0):
      hours=12.0
    result=[hours,temp,'AM',days]
  else:
    temp=leftMins%60
    hours=(leftMins-temp)/60
    result=[hours-12.00,temp,'PM',days]
    if(hours==12.00):
      result=[hours,temp,'PM',days]

  a=str(int(result[0]))
  b=str(int(result[1]))
  if(int(result[1])<=9):
    b="{0:02d}".format(int(result[1]))
    
  string=a+':'+b+" "+result[2]

  days=int(days)

  if(day!=' '):
    index=weekDays.index(day)
    index=index+days
    if(index>=7):
      index=index%7
    string=string+', '+weekDays[index]

  
  if(days!=0.0):
    if(days==1):
      string=string+' '+'(next day)'
    else:
      string=string+' '+'('+str(days)+' days later)'

  days=int(days)
  
  return string
