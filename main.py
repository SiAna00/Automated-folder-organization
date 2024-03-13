import os
import os.path

downloads_path = "C:/Users/asimi/Desktop/downloads_path"

if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)
    print("Created")

else:
    print("Exists")
