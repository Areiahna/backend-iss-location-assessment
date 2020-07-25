import requests
import re
import turtle
import time
# !/usr/bin/env python

__author__ = 'Areiahna Cooks, SE COACH KANO'

"""URL: http://api.open-notify.org/astros.json

    TODO:
       -   extract specific data from url
           -   Austronaut full names
           -   Spacecraft
           -   Total # of astronauts in space

       -   display the extracted data

   """
NAMES = r'(\w+\W\w+)'
SPACECRAFT = r'craft\W+\w+'
PASSENGERS = r'\d'


def get_astronauts():
    URL = 'http://api.open-notify.org/astros.json'
    response = requests.get(URL).text
    ISS = response.replace('"', '').replace('{', '').replace('}', '')

    display = []
    names = re.findall(NAMES, ISS)
    crafts = re.findall(SPACECRAFT, ISS)
    astronauts = re.findall(PASSENGERS, ISS)

    display.append(f'# of Astronauts: {astronauts[0]}')
    display.append(crafts[0])

    for name in names:
        display.append(name)
    return display


def get_coordinates():
    URL = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(URL).text
    response.replace("{", '').replace("}", '').replace("", '')

    TIME_STAMP = r'timestamp\W+(\d+)'
    LON = r'longitude\W+(\d+\W\d+)'
    LAT = r'latitude\W+(\d+\W\d+)'

    time = re.findall(TIME_STAMP, response)
    longit = re.findall(LON, response)
    latit = re.findall(LAT, response)
    x = latit[0]
    y = longit[0]
    display = [
        f'Timestamp: {time[0]} Latitude: {x} Longitude: {y}']
    print(display)

    return ((float(y)), float(x))


def get_indianapolis_coords():
    lat = 39.7684
    lon = -86.1581

    RISE_TIME = r'\d\d\d\d+'
    URL = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
    response = requests.get(URL).text
    response.replace("", '')

    indy_times = re.findall(RISE_TIME, response)
    next_visit = indy_times[0]

    return float(next_visit)


screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90,  180, 90)


bckg = "map.gif"
screen.bgpic(bckg)
image = "iss.gif"
screen.register_shape(image)


def main():

    display = get_astronauts()
    print('\n'.join(display))
    ISS_coords = get_coordinates()
    indy_time = get_indianapolis_coords()

    print(time.ctime(indy_time))

    ISS = turtle.Turtle()
    ISS.penup()
    ISS.shape(image)
    ISS.goto(ISS_coords)

    Indy_turtle = turtle.Turtle()
    Indy_turtle.penup()
    Indy_turtle.shape('circle')
    Indy_turtle.shapesize(.5, .5)
    Indy_turtle.color('yellow')
    Indy_turtle.goto(-86.15, 39.76,)
    Indy_turtle.write(time.ctime(indy_time), font=8)

    # Indy_turtle2 = turtle.Turtle()
    # Indy_turtle2.shape('circle')
    # Indy_turtle2.shapesize(1, 1)
    # Indy_turtle2.color('pink')
    # Indy_turtle2.goto(39.76, 86.15)
    turtle.done()


if __name__ == '__main__':
    main()
