import urllib.request
from bs4 import BeautifulSoup
import re

def main():
	c=1
	while(c<=41):
		data_read =openfile('page-'+str(c)+'.txt')
		c=c+1
		beautifulsoup(data_read)
		


def beautifulsoup(html_data):
	soup= BeautifulSoup(html_data,'html.parser')
	mydivs = soup.find_all("ul",{"class":"spojeni pack"})
	for x in mydivs[0].contents:
		for z in x.children:
			try:
				v=z.string
				if (v!="None"):
					writefile(v)
			except TypeError:
				continue
	writefile('\n')
	writefile('\n')

	
def writefile(scrape_data):
	f= open('details_1st_41.txt','a')
	try:
		temp_scrape= scrape_data.encode('utf-8')
		f.write(temp_scrape.decode('unicode-escape')+' '+'|'+' ')
	except AttributeError:
		pass
	f.close

def openfile(name_file):
	f= open(name_file,'r')
	whole_file=f.read()
	f.close
	return whole_file

def url_lib(url_r):
	url = 'http://www.zivefirmy.cz'+url_r
	req= urllib.request.Request(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
	resp= urllib.request.urlopen(req)
	data= resp.read()
	return data


if __name__ == '__main__':
	main()
