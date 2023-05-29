import os
file_list_all=os.listdir()
extension_names=[".srt",".tsv",".txt",".vtt",".json"]

for file in file_list_all:
    for ext in extension_names:
        if ext in file:
            os.remove(file)
