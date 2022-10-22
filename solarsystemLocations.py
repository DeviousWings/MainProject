# Begain on date: Oct 20 time: 1600.
# import solarsystem

# H = solarsystem.Heliocentric(year=2020, month=1, day=1, hour=12, minute=0 )

# planets_dict=H.planets()
# print('Planet','   \t','Longitude','   \t','Latitude','   \t','Distance in AU')
# for planet in planets_dict:
#     pos=planets_dict[planet]
#     print(planet,'   \t',round(pos[0],2),'   \t',round(pos[1],2),'   \t',round(pos[2],2))

# 1730 was finally able to get the information for each planet in the solar system.
import matplotlib.pyplot as plt
# import math
import datetime
import solarsystem
# import planetview
# from libraries.planetview import solarsystem

now    = datetime.datetime.now()
year   = now.year
month  = now.month
day    = now.day
# nameOfDay = now.strftime()
hour   = now.hour
minute = now.minute

# if (datetime.datetime.now(datetime.timezone.utc).dst())==None:
#     dst=0
# else:
#     dst=1
dst = 0

print(f"{now:%a, %d %b %Y}, {hour}:{minute}")

# planet position output be in horizontal coordinates (longitude, latitude, distance from sun in AU)
view='horizontal'
H = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute, dst=dst, view=view )

planets=H.planets()
distances=[]
print('Planet', '   \t','Longitude', '  \t','Latitude', '   \t','Distance')
print('-------------------------------------------------------------------')
for key in planets:
    distances.append(planets[key][2])
    elements = planets[key]
    print(key, '   \t',round(elements[0],2), '  \t',round(elements[1],2), '   \t',round(elements[2],2))
print()
print('Distance is in AU')