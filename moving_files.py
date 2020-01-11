import os
import time
import random as r

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    """Track the folder_to_track and when folder has been modified
    move all the files in folder_new_place with new name
    """
    _num_of_file = r.randint(1, 9999)

    def on_modified(self, event):
        exp = event.src_path.split('.')[-1]
        for filename in os.listdir(folder_to_track):
            self._num_of_file += 1
            new_name = f'перемещено_адвокатом_{str(self._num_of_file)}.{exp}'
            src = f'{folder_to_track}/{filename}'
            new_place = f'{folder_new_place}/{new_name}'
            time.sleep(.5)
            os.rename(src, new_place)


if __name__ == '__main__':
    folder_to_track = input('Enter an absolute path to track\n> ')
    folder_new_place = input('Enter an absolute path to new place of files\n> ')

    handler = FileHandler()
    observer = Observer()
    observer.schedule(handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()