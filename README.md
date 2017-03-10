# download-tegna-video

* used to download the video from http://www.kens5.com/news/local/104700-texas-taxpayers-owed-115-million-in-refunds-from-2013/419618114 using python
* merge them into one .ts file using ffmpg
* and convert them into a .mp4 file using ffmpeg

# change permissions
```
chmod +x merge.sh
chmod +x ts2mp4.sh
```

# usage
```
python download.py
./merge.sh
./ts2mp4.sh
```

# TODO
```
detect .ts links if given tegna/akami url
```
