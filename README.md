# Pythonhunter-transcription

捕蛇者说文字稿

## 温馨提示

+ large模型占用空间约2G，请注意预留充足SSD空间。
+ 批量转的vtt可能没有毫秒。

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

见 `/src/merge_and_download.py` 

### 文本处理

**使用Whisper转换文本**

```shell
whisper ep0.mp3 --language=Chinese --model large --initial_prompt="以下是普通话的句子。"
```

**清理不需要的多格式输出文件**

我们假设你直接从Terminal里面复制文本（而不是输出到文件（或者输出到`.srt`/`.tsv`/`.txt`/`.vtt`/`.json`以外的格式））

见 `/src/cleanup.py` 

**VTT转whisper格式**

见 `/src/vtt_2_whisper.py` 