from enum import Enum

class Events(str, Enum):
    event600 = '600m'
    event800 = '800m'
    event1000 = '1000m'
    event1500 = '1500m'
    eventMile = 'Mile'
    event2000 = '2000m'