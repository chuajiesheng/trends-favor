import feedparser

rss = feedparser.parse('http://www.channelnewsasia.com/rss/latest_cna_frontpage_rss.xml')

title = rss['feed']['title']
print 'title:', title
link = rss['feed']['link']
print 'link:', link
updated = rss['feed']['updated']
print 'updated:', updated
sub = rss.feed.subtitle
print 'sub:', sub
ver = rss.version
print 'ver:', ver
len = len(rss['entries'])
print 'length:', len
header = rss.headers
print 'header:', header

print '\n'

for post in rss.entries:
    print post.title + '\n'
    print post.link + '\n'
    print '\n'
