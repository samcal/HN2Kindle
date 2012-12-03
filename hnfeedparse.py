import feedparser

def main():
	hn = feedparser.parse('http://news.ycombinator.com/rss')
	for article in hn['entries']:
		print "Title: %s" % article['title']

if __name__ == '__main__':
	main()