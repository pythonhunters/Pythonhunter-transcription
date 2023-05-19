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
```

### 文本处理

**使用Whisper转换文本**
```shell
whisper ep0.mp3 --language=Chinese --model large --initial_prompt="以下是普通话的句子。"
```

large模型占用空间约2G，请注意预留充足SSD空间。

