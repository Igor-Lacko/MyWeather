"""Contains the database of supported cities from worldcities.csv.\n
TODO: Add attribution"""
import pandas



cities = pandas.read_csv(filepath_or_buffer='Assets/worldcities.csv', usecols=[0])
database = [city[0] for city in cities.values]

database.append('Presov')       #why wasn't it there in the first place? :((
database.append('Current')      #Can't forget about this one