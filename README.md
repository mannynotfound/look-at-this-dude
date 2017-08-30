# look at this dude

Wrapper around `moviepy` to programatically create ["look at this dude"](https://www.youtube.com/watch?v=fhnF8R6_q70) style roast videos.

## usage

pass a directory that contains nothing but the images you want to use. By default, the script will use the alphabetic order of the 
first 12 files to determine the order of the slideshow.

```bash
python latd.py -i src/ -o data/look_at_this_dude.mp4
```

## dependencies

(mac)
```
brew install imagemagick
```

```bash
pip install -r requirements.txt
```
