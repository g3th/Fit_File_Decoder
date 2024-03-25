import os
from pathlib import Path

class DiskOperations:

    def __init__(self, filename):
        self.path = str(Path(__file__).parent) + "/fit_files/"
        self.filename = filename
        os.makedirs(self.path, exist_ok=True)

    def open_file(self):
        bytes_list = []
        with open(self.path + self.filename, 'rb') as bytes_data:
            for i in bytes_data.read():
                bytes_list.append(i.to_bytes().hex())
        return bytes_list

    def save_data(self):
        print("One Day it will happen...")