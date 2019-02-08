try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
 

def get_link(message):
	# to search 
	query = "linked in "+message
	  
	url=[]

	for i in  search(query, tld="com", num=1, stop=1, pause=2): # change num range to fetch more result
		print(i)
		url.append(i)
	return url

# get_link("AJ vekata krishnan")