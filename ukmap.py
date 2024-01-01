import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Read the dataset into a DataFrame
df = pd.read_csv("Growlocations.csv")

# Swap Latitude and Longitude columns to match the naming in the provided dataset
df['Latitude'],df['Longitude']= df['Longitude'],df['Latitude']

# Verify and clean the dataset
# Remove leading/trailing whitespaces from column names
df = df.rename(columns=lambda x: x.strip())  

# Filter locations within the specified bounding box
bbox = {
    'min_lon': -10.592,
    'max_lon': 1.6848,
    'min_lat': 50.681,
    'max_lat': 57.985
}
df = df[(df['Longitude'] >= bbox['min_lon']) & (df['Longitude'] <= bbox['max_lon']) &
        (df['Latitude'] >= bbox['min_lat']) & (df['Latitude'] <= bbox['max_lat'])]

# Plot the sensor locations on the provided image
uk_map_image = Image.open("map7.png")  

# Create a scatter plot with custom x-axis and y-axis
fig, ax = plt.subplots()
ax.imshow(uk_map_image, extent=[bbox['min_lon'], bbox['max_lon'], bbox['min_lat'], bbox['max_lat']])

# Adjust marker size and style
ax.scatter(df['Longitude'], df['Latitude'], color='red', marker='o', s=5, label='Sensor Locations')

# Set plot labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Sensor Locations on UK Map')

# Display legend
ax.legend()

#show the plot
plt.show()
