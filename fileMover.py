import os
import time
import shutil

# For instantaneous file transfer set the time_gap variable to 0
time_gap = 10

def ConsoleUi():
    print('')
    print("\033[4mTransporter Started:\033[0m")
    print("Your files will be moved in realtime")
    print("Press Ctrl + C to stop anytime...")

def FileMover(src_folder, dst_folder):
    files_list = os.listdir(src_folder)

    for file in files_list:
        destination_path = os.path.join(dst_folder,file)
        original_path = (src_folder + '\\' + file)
        if os.path.isfile(original_path):
            shutil.move(original_path, destination_path)

src_folder = ".\\Demo_Folder\\Original_Destination"
dst_folder = ".\\Demo_Folder\\Final_Destination"

ConsoleUi()

try:
    while True:
        FileMover(src_folder,dst_folder)
        time.sleep(time_gap)
        x = True

except KeyboardInterrupt:
    print('')