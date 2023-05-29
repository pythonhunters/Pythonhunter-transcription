import requests
import os

meta_url_file = open("meta_url.txt", "r")
meta_title_file = open("meta_title.txt", "r", encoding="utf-8")
meta_url_data = list(filter(bool, meta_url_file.read().split("\n")))
meta_title_data = list(filter(bool, meta_title_file.read().split("\n")))
for i in range(len(meta_title_data)):
    if "Ep" in meta_title_data[i]:
        meta_title_data[i] = (
            "ep"
            + meta_title_data[i]
            .split(".")[0]
            .replace("Ep ", "")
            .replace(" ", "")
            + ".mp3"
        )
    elif "特别篇" in meta_title_data[i]:
        meta_title_data[i] = (
            meta_title_data[i].replace("[", "").replace(" ", "") + ".mp3"
        )  # 会根据获取标题的bash命令更新而修订本行规则
    else:
        meta_title_data[i] += ".mp3"

meta_url_file.close()
meta_title_file.close()

if len(meta_url_data) == len(meta_title_data):
    for i in range(len(meta_url_data)):
        if os.path.exists(meta_title_data[i]) == False:
            this_volume_file = open(meta_title_data[i], "wb")
            result = requests.get(url=meta_url_data[i])
            this_volume_file.write(result.content)
            this_volume_file.close()