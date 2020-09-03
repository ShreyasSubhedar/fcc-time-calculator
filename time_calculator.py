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


  
  return None