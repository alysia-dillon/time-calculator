import math

def add_time(start, duration, day_of_week=False):

  # day variables
  days_of_the_week_index = {"monday":0, "tuesday":1,"wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
  # start variables
  start_hours = start.split(":")[0]
  start_minutes = start.split(":")[1].split(" ")[0]
  
  # AM PM variables
  AM_or_PM = start.split(" ")[1]
  AMPM_flip = {"AM":"PM", "PM":"AM"}
  
  # duration variables
  duration_hours = duration.split(":")[0]
  duration_minutes = duration.split(":")[1]
  
  # total variables + logic
  total_days = math.floor(int(duration_hours) / 24)
  total_minutes = int(start_minutes) + int(duration_minutes)
  
  if(total_minutes >= 60):
    start_hours = int(start_hours) + 1
    total_minutes = int(total_minutes) % 60

  amount_of_AMPM_flips = (int(start_hours) + int(duration_hours)) / 12
  total_hours = (int(start_hours) + int(duration_hours)) % 12

  total_minutes = total_minutes if total_minutes > 9 else "0" + str(total_minutes)
  total_hours = total_hours = 12 if total_hours == 0 else total_hours
  
  if(str(AM_or_PM) == "PM" and int(start_hours) + (int(duration_hours) / 12) >= 12):
   total_days += 1

  AM_or_PM = AMPM_flip[AM_or_PM] if math.floor(amount_of_AMPM_flips) % 2 == 1 else AM_or_PM

  returnTime = str(total_hours) + ":" + str(total_minutes) + " " + AM_or_PM

  if(day_of_week):
    day_of_week = day_of_week.lower()
    index = (int(days_of_the_week_index[day_of_week]) + total_days) % 7
    new_day = days_of_the_week_array[index]
    returnTime += ", " + new_day

  print("# of total days: " + str(total_days))
  
  if(int(total_days) == 1):
    return returnTime + " " + "(next day)"
  elif(total_days > 1):
    return returnTime + " (" + str(total_days) + " days later)"
  else:
    return returnTime