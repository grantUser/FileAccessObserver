import os
import time

class FileAccessObserver:
    def __init__(self, directory):
        self.directory = directory
        self.creation_time = time.time()
        self.access_times = {}

    def start_observing(self):
        while True:
            new_access_times = {}
            for filename in os.listdir(self.directory):
                filepath = os.path.join(self.directory, filename)
                if os.path.isfile(filepath):
                    stat_info = os.stat(filepath)
                    access_time = stat_info.st_atime
                    new_access_times[filename] = access_time
                    if access_time > self.creation_time:
                        if access_time != self.access_times.get(filename):
                            self.handle_file_access(filename, access_time)

            self.access_times = new_access_times
            time.sleep(0.2)

    def handle_file_access(self, filename, access_time):
        print(f"New file accessed: {filename}, Access time: {access_time}")

directory_path = 'C:\\Users\\***\\Desktop\\test24\\ok\\'
observer = FileAccessObserver(directory_path)
observer.start_observing()
