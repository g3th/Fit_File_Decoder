from draw_map import DrawMap
from disk_operations import DiskOperations
from decoder import DecodeFile

# Examples - will be command line arguments:

disk = DiskOperations("5.fit") # FIT file name - must be placed in "fit_files" folder
bytes_list = disk.open_file() # Open file
decoder = DecodeFile(bytes_list) # Decode Information
distance = decoder.extract_distance() # Any method - i.e. distance, speed, average pace, title etc..
long_lat_list = decoder.extract_long_and_lat_and_convert_semicircles() # Get route long-lat to use with folium
start_points = int((len(long_lat_list) - 1) / 2) # Start map roughly in the middle of the route

# Add Folium Points and Generate
generate_map = DrawMap(long_lat_list[start_points][0], long_lat_list[start_points][1], 12.5, 3, 1200, 1200)
colour = 'black'
for i in range(len(long_lat_list)):
    if i == int((len(long_lat_list) - 1) / 2):
        colour = 'red'
    generate_map.create_points(long_lat_list[i], long_lat_list[i], colour)
# Inject HTML div into existing map html
generate_map.popup_with_run_info("Total Distance: {} km".format(distance[len(distance) - 1]))
# Draw
generate_map.draw()


