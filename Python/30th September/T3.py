hours = int(input("What time is it in hours? (digital) "))
minutes = int(input("What time is it in minutes? "))
seconds = int(input("What time is it in seconds? "))
s = hours*60*60 + minutes * 60 + seconds
print(f"The time is {hours}:{minutes}:{seconds}")
print(f"That is {s} seconds into the day")
