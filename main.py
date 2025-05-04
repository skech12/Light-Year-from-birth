import time
import datetime


r = 0 #sekunder
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))
hour = int(input("Hour (0–23): "))
minute = int(input("Minute (0–59): "))
second = int(input("Second (0–59): "))
microsecond = int(input("Microsecond (0–999999): "))


fullBorn = datetime.datetime(year, month, day, hour, minute, second, microsecond)

lightKMPerSecond = 299_792.458
seconds_per_year = 365.25 * 24 * 3600

while True:
    now = datetime.datetime.now()
    delta = now - fullBorn
    seconds_elapsed = delta.total_seconds()
    distance_km = seconds_elapsed * lightKMPerSecond
    distance_ly = seconds_elapsed / seconds_per_year
    

    print(f"{distance_km:,.3f} km")
    print(f"{distance_ly:.6f} lysår")
    time.sleep(1)
