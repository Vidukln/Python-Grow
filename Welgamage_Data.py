#W.S.V.Lakshan - 2551074
#This python code will plot grow locations of the sensor data
#Latitude and longitude labels were marked incorrectly in the original CSV dataset
#First corrected the labels on the data set

#Importing required Libraries
#Pandas library will allow operations related to dataframe handling
#Matplotlib will help to create visualization
#matplotlib.offsetbox will help to add images and handle them.
#In my case UK map provided
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#Reading my CSV data into the dataframe
df = pd.read_csv("GrowLocations.csv")

#Some location values are way outside the allowed values for latitude and Longitude
#This line will fillter data point which lies inside the given boundaries for longitude and latitude
#Reference: Pandas Documentation - https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-comparison
df = df[(df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985) & (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)]

#Loading the UK map
#Matplotlib Documentation
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html
#This will be stored as a numpy array
base_uk_map = plt.imread("map7.png")

#Create a Matplotlib figure and axis
#This will be the map container
#UK map is displayed and all senson locations are dispaled on it at once
#Subplot will help to map all the locations in one canvas created by this
fig, ax = plt.subplots(figsize=(10, 10))

#Creating the map image with given boundaries
#Matplotlib Documentation
#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html
ax.imshow(base_uk_map, extent=[-10.592, 1.6848, 50.681, 57.985])

#Plot the sensor locations on the map
for index, row in df.iterrows():
  x, y = row['Longitude'], row['Latitude']
  ax.plot(x, y, marker='o', markersize=5, color='red')

#Below lines will display the map of UK with sensor locations on it
#title, x axis and y axis labels are defined as below
plt.title('Sensor Locations of GROW Data')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
