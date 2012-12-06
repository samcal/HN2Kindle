HN2Kindle
=========

HN2Kindle is a conglomeration of resources that allow for the downloading of all articles in Hacker News and converting them to the MOBI format, which is compatible with the Kindle.

The script takes ~6 minutes to run.

Tips
----

### Crontab
You can run HN2Kindle as a cronjob, so that the script will download the news by itself, on a schedule. To add a cronjob that will run the HN2Kindle script everyday at 7AM, first type:

    crontab -e

then add the line:

    0 7 * * * cd ~/dir/to/HN2Kindle; sh hn2kindle.sh

Dependencies
------------

- <a href='http://code.google.com/p/python-epub-builder/'>python-epub-builder</a>
- <a href='http://code.google.com/p/feedparser/'>feedparser</a>
- <a href='http://lxml.de'>lxml</a>
- <a href='http://genshi.edgewall.org/'>genshi</a>
- <a href='http://calibre-ebook.com/'>Calibre</a> command line tools
