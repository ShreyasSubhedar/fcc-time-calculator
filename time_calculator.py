def add_time(start, duration,day="Anyday"):
  # Getting useful data from start string
  timely,midday= start.split()
  hour,minutes = timely.split(':')
  hour= int(hour)
  minutes = int(minutes)
  # Making the clock into 24 hour format
  if midday == "PM":
    hour += 12
  
  # Getting data from duration 
  duration_hour,duration_minutes = duration.split(':')
  duration_hour = int(duration_hour)
  duration_minutes = int(duration_minutes)

  # Calculating total hours, minutes 
  total_minutes = minutes + duration_minutes
  ans_minutes = total_minutes % 60
  extra_hours = total_minutes // 60
  total_hour = hour+ duration_hour +extra_hours
  # final hours as per 12 Hour clock
  ans_hour = (total_hour % 24) % 12
  if ans_hour == 0:
    ans_hour =12
  # 
  total_day = (total_hour // 24)
  # deciding mid day
  ans_midday=""
  if (total_hour%24) <=11:
    ans_midday="AM"
  else:
    ans_midday="PM"
  if ans_minutes<=9:
    ans_minutes = '0'+str(ans_minutes)
  else:
    ans_minutes = str(ans_minutes)

  if total_day == 0 :
    return str(ans_hour)+":"+ans_minutes+' '+ans_midday 
  if total_day == 1:
    return str(ans_hour)+":"+ans_minutes+' '+ans_midday +' (next day)'
  ans = str(ans_hour)+":"+ans_minutes+' '+ans_midday+' ('+ str(total_day)+' days later)'
  return ans