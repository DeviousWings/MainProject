from msilib.schema import LaunchCondition
import planet_locations


def main():
    
    mars = input("What is Mars' location: ")
    # Import moon

    print('Go to TheSkyLive.com to get moon location')
    print()
    rightAscension = input('What is the Right Ascension HH:MM: ').split()
    degree = input("In Declination what is the degrees: ")
    lat = input('In Declination what is the Latitude: ')
    lon = input('In Declination what is the Longitude: ')
    const = input('What is the Constellation: ')

    
    time = timeLaunch(rightAscension)
    
    # declination = hour:min
    print(f"Moon Right Ascension: {time}")
    print(f"Declination: {degree}° {lat}' {lon}''")
    print(f"The Constellation is {const}")
    print(f"Mars is at: {mars}°")

def timeLaunch(rightAscension):

    
    for time in rightAscension:
        hour,min = [int(i) for i in time.split(':')]
        
        
        if hour == 20:
            print('Launch is a go')
        else:
            print('No go for Launch')
        
        if min == 30:
            print('Launch is a go')

        else:
            print('No go for Launch')
        return time
    
    # if degree == 10:
    #     go Launch
    # else:
    #     No go
    #     return degree
        
    # if lat == 136:
    #     Go Launch
    # else:
    #     No Go
    #     return lat        
        
    # if lon == 150:
    #     go Launch
    # else:
    #     no go
    #     return lon
        
    # if const == 'Virgo':
    #     Go Launch
    # else:
    #     No go
    #     return const
        
    # if mars == 180:
    #     go Launch
    # else:
    #     No go
    #     return mars
    
    

    
    
if __name__ == '__main__':
    main()