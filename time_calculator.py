def add_time(start, duration,day="Anyday"):
  # Getting useful data from start string
  timely,midday= start.split()
  hour,minutes = timely.split(':')
  hour= int(hour)
  minutes = int(minutes)
  if midday == "PM":
    hour += 12
  return None