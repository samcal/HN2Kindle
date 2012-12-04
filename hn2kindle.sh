path=`python hnfeedparse.py`
ebook-convert "$path.epub" "$path.mobi"