"""This script performs a google search to fetch LinkedIn Url"""
try:
	from googlesearch import search
except ImportError:
	print "No module named 'google' found"

def get_link(message):
	"""Search LinkedIn Url"""
	query = "linked in "+message
	query = query.encode('utf8')
	url = []
	for i in search(query, tld="com", num=10, stop=1, pause=2):
		url.append(i)
	return url
