
import re
import ez_epub
import feedparser
import urllib
import readability
from datetime import date

header_re = re.compile(r'h[1-6]')

def hn_articles():
	hn = feedparser.parse('http://news.ycombinator.com/rss')
	return hn['entries']

def parse_article(article):
	html = urllib.urlopen(article['link']).read()
	text = readability.Document(html).summary()
	text = re.sub(r'<[^>]+>', '', text)
	text = re.sub(r'&#(\d+);', lambda m:unichr(int(m.group(1))), text)

	return (article['title'], text)

def all_sections():
	sections = []
	for article in hn_articles():
		clean_article = parse_article(article)
		if clean_article:
			section = ez_epub.Section()
			section.title = clean_article[0]

			section.text.append(clean_article[1])
			sections.append(section)

	return sections

if __name__ == '__main__':
	book = ez_epub.Book()
	book.title = 'Hacker News %s' % date.today().isoformat()
	book.authors = ['Sam Calvert']
	book.sections = all_sections()
	path = r'EPubs/%s' % book.title
	book.make(path)
	print path