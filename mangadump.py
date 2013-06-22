import sys
from sys import argv
import urllib2
from bs4 import BeautifulSoup
import os

#url="http://www.onemanga.me/the-world-god-only-knows/"
arr=[]
arr2=[]

def scrape_onemanga(url="http://www.onemanga.me/the-world-god-only-knows/"):

	if not url:
		print "Please supply url to be downloaded"

	path = os.getcwd() + '/mangadump/' + url.split('/')[-2]

	if not os.path.exists(path):
	    os.makedirs(path)
	    print "Created directory " + path

	soup = BeautifulSoup( urllib2.urlopen(url).read() )


	for i in soup.find_all('a',{'class' : 'lst'})[::-1]:

		volume_link = i.get("href")
		arr.append(volume_link)
		path_temp = path +'/'+ volume_link.split('/')[-2]
		#print volume_link.split('/')
		if not os.path.exists(path_temp):
		    os.makedirs(path_temp)
		    print 'Created Directory ' + path_temp

		print 'Now Downloading Volume ' + volume_link.split('/')[-2] +' at ' + path_temp   
		soup = BeautifulSoup( urllib2.urlopen(volume_link).read() )

		k = soup.find('h2',{'class' : 'wpm_tip lnk_cnr'})

		for p in k.find_all('a'):
			page_link = p.get('href')
			arr2.append(page_link)

			soup = BeautifulSoup( urllib2.urlopen(page_link).read() )
			t=soup.find('img',{'class' : 'manga-page'})
			
			img_link = t.get('src') 
			
			
			img_path = path +'/'+ page_link.split('/')[-3] +'/'+ page_link.split('/')[-2] + '.jpg'
			
			if os.path.isfile(img_path) == False:
				u = urllib2.urlopen(img_link)
				data = u.read()
				print "Saving " + img_link +" at " + img_path
				f=open(img_path , "wb")
				f.write(data)
				f.close()
			else :
				print 'Skipping image already exists at location '	+ img_path


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print scrape_onemanga()
	else: 
		print scrape_onemanga(argv[1])
'''
TODO

Supply arguments of url via command line (DONE)
Accomodate more manga sites besides onemanga

'''

