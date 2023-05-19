# Pythonhunter-transcription

捕蛇者说文字稿

## 参考代码

### 获取篇目

可访问 https://pythonhunter.org/feed/audio.xml 获取所有过往播客内容

**获取URL**

```bash
curl -s https://pythonhunter.org/feed/audio.xml | grep -oE 'enclosure url="([^"]+)"' | cut -d\" -f 2 > meta_url.txt
```

**获取标题**

```bash
curl -s https://pythonhunter.org/feed/audio.xml | grep -oP '<title>\s*<!\[CDATA\[\K[^]]*' > meta_title.txt
```

请注意，这样获取的title在特别篇并不完整，并且存在一些不是title的也被扩充进来，请手动校对令其和url一样长（尚未自动化）

**合并与下载**
```python
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
```

### 文本处理

**使用Whisper转换文本**
```shell
whisper ep0.mp3 --language=Chinese --model large --initial_prompt="以下是普通话的句子。"
```

large模型占用空间约2G，请注意预留充足SSD空间。

