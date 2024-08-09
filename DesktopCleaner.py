import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CleanDesk(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(tracking_folder):
            i = 1
            if file_name != 'Files':
                new_name = file_name
                current_file = os.path.isfile(destination_folder + '/' + new_name)
                while current_file:
                    i += 1
                    new_name = os.path.splitext(tracking_folder + '/' + new_name)[0] + str(i) + os.path.splitext(tracking_folder + '/' + new_name)[1]
                    new_name = new_name.split("/")[4]

                src = tracking_folder + "/" + file_name
                new_name = destination_folder + "/" + new_name
                os.rename(src, new_name)



tracking_folder = '/Users/jasonwhite/Desktop'
destination_folder = '/Users/jasonwhite/Desktop/files'
event_handler = CleanDesk()
observer = Observer()
observer.schedule(event_handler, tracking_folder, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()