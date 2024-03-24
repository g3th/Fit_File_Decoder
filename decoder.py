import ctypes


class DecodeFile:

    def __init__(self, b_list):
        self.b_list = b_list
        self.block = []

    def append_list(self, index):
        self.block.append([self.b_list[index], self.b_list[index + 1], self.b_list[index + 2], self.b_list[index + 3], self.b_list[index + 4],
                           self.b_list[index + 5],self.b_list[index + 6],self.b_list[index + 7],self.b_list[index + 8],self.b_list[index + 9]])

    def long_lat_block(self):
        for j in range(len(self.b_list)):
            try:
                if "d4" in str(self.b_list[j]) and "3b" in str(self.b_list[j + 1]) and "ff" in str(self.b_list[j + 9]):
                    if "ff" not in (self.b_list[j + 6], self.b_list[j + 7], self.b_list[j + 8]):
                        self.append_list(j)
            except IndexError:
                break

    def extract_long_and_lat_and_convert_semicircles(self):
        self.long_lat_block()
        result = []
        for j in self.block:
            temp_lat = int("{}{}{}{}".format(j[5], j[4], j[3], j[2]), 16)
            temp_lon = ctypes.c_int32(int("{}{}{}{}".format(j[9], j[8], j[7], j[6]), 16)).value
            result.append([self.conversion_to_degrees(temp_lat), self.conversion_to_degrees(temp_lon)])
        self.block = []
        return result

    def distance_block(self):
        for j in range(len(self.b_list)):
            # byte group could be (i.e):
            # '0xa6, 0x??, 0x??, 0xc2, 0xff'
            # and distance values
            if "a" in str(self.b_list[j]):
                try:
                    if "ff" in str(self.b_list[j + 5]) and "00" in str(self.b_list[j + 9]):
                        self.append_list(j)
                except IndexError:
                    break
    # Converts Garmin's semicr
    def conversion_to_degrees(self, val):
        return val * (180 / pow(2, 31))

    def speed_block(self):
        for j in range(len(self.b_list)):
            if "c2" in str(self.b_list[j]):
                try:
                    if "ff" in str(self.b_list[j + 1]) and "00" in str(self.b_list[j + 5]):
                        self.append_list(j)
                except IndexError:
                    break

    def extract_speed(self):
        self.speed_block()
        speed = []
        pace_list = []
        for j in self.block:
            temp = "{}{}".format(j[7], j[6])  # Little Endian
            speed.append(int(temp, 16) / 1000)
        self.block = []
        for k in speed:
            pace_list.append(self.meters_per_second_to_pace(k))
        del (pace_list[len(pace_list) - 1], pace_list[len(pace_list) - 1],)  # Deletes last two unrelated entries in list
        return pace_list

    def meters_per_second_to_pace(self, value):
        kms_per_minute = 1000 / (value * 60)
        minutes = int(kms_per_minute)
        seconds = int((kms_per_minute % 1) * 60)
        if seconds < 10:
            return "{}:0{}".format(minutes, seconds)
        else:
            return "{}:{}".format(minutes, seconds)

    def extract_distance(self):
        self.distance_block()
        convert = []
        for j in self.block:
            temp = "{}{}{}".format(j[8], j[7], j[6])  # Little Endian
            convert.append(int(temp, 16) / 100) # Converts from hex to int in Km
        del (convert[len(convert) - 1], convert[len(convert) - 1],) # Deletes last two unrelated entries in list
        self.block = []
        return convert
