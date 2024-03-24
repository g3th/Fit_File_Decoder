from disk_operations import DiskOperations
from decoder import DecodeFile

disk = DiskOperations("4.fit")
disk.create_folders()
bytes_list = disk.open_file()
decoder = DecodeFile(bytes_list)
long_lat_list = decoder.extract_long_and_lat_and_convert_semicircles()
distance_list = decoder.extract_distance()
print(decoder.extract_speed())
