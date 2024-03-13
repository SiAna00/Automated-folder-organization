import os
import os.path
import shutil

downloads_path = "C:/Users/asimi/Downloads"

filetypes = {
    "Audio": [".m4a", ".wav", ".flac", ".mp3", ".wma"],
    "Vid": [".mp4", ".mov", ".wmv", ".avi", ".flv", ".mkv"],
    "Img": [".gif", ".jpeg", ".jpg", ".png", ".svg"],
    "Docs": [".doc", ".docx", ".html", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".epub"],
    "Other": [".exe"]
}

for item in os.listdir(downloads_path):
    for key in filetypes:
        for extension in filetypes[key]:
            if item.endswith(extension):
                if not os.path.exists(f"{downloads_path}/{key}"):
                    os.makedirs(f"{downloads_path}/{key}")
                    shutil.move(f"{downloads_path}/{item}", f"{downloads_path}/{key}/{item}")

                else:
                    shutil.move(f"{downloads_path}/{item}", f"{downloads_path}/{key}/{item}")
            else:
                print("Unknown extension.")
