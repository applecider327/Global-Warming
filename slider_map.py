# Required: Plotly. To install one, simply type in "pip install plotly==4.7.1" in a terminal.
# The end result should be three different images/graphs in three different tabs.

Cell 1:
import numpy as np
import pandas as pd

Cell 2:
import plotly.graph_objs as go
import plotly.io as pio

Cell 3:
temp_hist_by_country = pd.read_csv("https://raw.githubusercontent.com/datares/climate_change/master/temp_hist_by_country(yearly).csv")

Cell 4:
temp_hist_by_country.iloc[:, 1] = temp_hist_by_country["Average Temperature (Celsius)"].apply(round, args = (2, ))

Cell 5:
temp_hist_by_country

Cell 6:
year = 1910

Cell 7:
scl = [[0.11, '#ff0000'], [0.22, '#0099cc'], [0.33, '#33ccff'], [0.44, '#99e6ff'], [0.55, '#ffffff'], 
       [0.66, '#ffbb99'], [0.77, '#ff7733'], [0.88, '#cc4400'], [0.99, '#0000ff']]
       
Cell 8:
countries = temp_hist_by_country.loc[temp_hist_by_country["Year"] == year, "Country"]

Cell 9:
avgt = temp_hist_by_country.loc[temp_hist_by_country["Year"] == year, "Average Temperature (Celsius)"]

Cell 10: 
data = [dict(
            type = 'choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = countries,
            text = "Average Temperature (Celsius)",
            z = avgt,
            locationmode = 'country names',
            marker = dict(line = dict(color = 'rgb(0,0,0)', width = 2)),
            colorbar = dict(title = 'Temperature, Celsius')
            )
       ]
       
Cell 11:
layout = dict(
    title = 'Average Temperature by Country, 1910',
    geo = dict(showframe = False,
               showocean = True,
               oceancolor = 'rgb(0,255,255)',
               projection = dict(type = 'orthographic'),
              )
             )
             
Cell 12:
fig = dict(data = data, layout = layout)

Cell 13:
pio.write_html(fig, file = 'graph1.html', auto_open = True)

Cell 14:
data_slider = []

Cell 15:
for each_y in temp_hist_by_country.Year.unique():
    data_one_year = dict(type = 'choropleth',
                         colorscale = scl,
                         autocolorscale = False,
                         locations = countries,
                         text = "Year: " + str(each_y),
                         z = temp_hist_by_country.loc[temp_hist_by_country["Year"] == each_y, "Average Temperature (Celsius)"],
                         zmin = -20,
                         zmax = 30,
                         locationmode = 'country names',
                         marker = dict(line = dict(color = 'rgb(0,0,0)', width = 1)),
                         colorbar = dict(title = 'Temperature, Celsius')
                        )
    data_slider.append(data_one_year)
    
Cell 16:
steps = []

Cell 17:
for i in range(len(data_slider)):
    step = dict(method = 'restyle',
                args = ['visible', [False] * len(data_slider)],
                label = 'Year {}'.format(i + 1910)) 
    step['args'][1][i] = True
    steps.append(step)
    
Cell 18:
sliders = [dict(active = 0, pad = {"t": 1}, steps = steps)]  

Cell 19:
layout = dict(
              title = 'Average Annual Temperature by Country, 1910-2012',
              geo = dict(showframe = False,
                         showocean = True,
                         oceancolor = 'rgb(0,255,255)',
                         projection = dict(type = 'orthographic'),
                        ),
              sliders = sliders
             )
             
Cell 20:
fig = dict(data = data_slider, layout = layout) 

Cell 21:
pio.write_html(fig, file = 'graph2.html', auto_open = True)

Cell 22:
scl2 = [[0.25, '#ffffff'],[0.50, '#ff8080'],[0.75, '#ff0000'],[1.00, '#800000']]

Cell 23:
past = temp_hist_by_country.loc[temp_hist_by_country["Year"] == 1910, "Average Temperature (Celsius)"]

Cell 24:
data_slider2 = []

Cell 25:
for each_y in temp_hist_by_country.Year.unique():
    data_one_year = dict(type = 'choropleth',
                         colorscale = scl2,
                         autocolorscale = False,
                         locations = countries,
                         text = "Year: " + str(each_y),
                         z = temp_hist_by_country.loc[temp_hist_by_country["Year"] == each_y, "Average Temperature (Celsius)"].values - past.values,
                         zmin = -5,
                         zmax = 5,
                         locationmode = 'country names',
                         marker = dict(line = dict(color = 'rgb(0,0,0)', width = 1)),
                         colorbar = dict(title = 'Change in Temperature, Celsius')
                        )
    data_slider2.append(data_one_year)
    
Cell 26:
steps2 = []

Cell 27:
for i in range(len(data_slider2)):
    step = dict(method = 'restyle',
                args = ['visible', [False] * len(data_slider)],
                label = 'Year {}'.format(i + 1910)) 
    step['args'][1][i] = True
    steps2.append(step)
    
Cell 28:
sliders2 = [dict(active = 0, pad = {"t": 1}, steps = steps2)]  

Cell 29:
layout2 = dict(
              title = 'Average Annual Temperature by Country, 1910 vs. Future Year',
              geo = dict(showframe = False,
                         showocean = True,
                         oceancolor = 'rgb(0,255,255)',
                         projection = dict(type = 'equirectangular'),
                        ),
              sliders = sliders2,
             )
             
Cell 30:
fig2 = dict(data = data_slider2, layout = layout2) 

Cell 31:
pio.write_html(fig2, file = 'graph3.html', auto_open = True)
