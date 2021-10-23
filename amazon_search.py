'''Python Program - Amazon Search by DJ Harshit'''

# Importing the modules
import requests
import bs4
import threading
import os

# Function to parse 1st type of webpage
def parse_1(soup):
	x = soup.find_all('div', 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20')	# Finding all the results

	for i in x:
		try:	# Handling the errors
			n1 = i.find('span', 'a-size-base-plus a-color-base')
			n2 = i.find('span', 'a-size-base-plus a-color-base a-text-normal')
			print(n1.string, n2.string)

			p = i.find('span', 'a-offscreen')
			print(p.string, '\n')

		except:
			... 	# Next iteration if error

# Function to parse 2nd type of webpage
def parse_2(soup):
	x = soup.find_all('div', 'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20')	# Finding all the results

	for i in x:
		try:	# Handling the errors
			n = i.find('a', 'a-link-normal a-text-normal')	# Find the name of product
			print(n.span.string)

			p = i.find('span', 'a-offscreen')	# Find the price of product
			print(p.string, '\n')

		except:
			... 	# Next iteration if error

os.system('cls')
txt = input('What do you want to search: ')
txt = '+'.join(txt.split())		# Replacing <space> with <+> in URL

# UA Proxy
hdrs = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}
url = f'https://www.amazon.in/s?k={txt}'

res = requests.get(url, headers=hdrs)	# Requesting the html

soup = bs4.BeautifulSoup(res.text, 'html.parser')	# Parsing the html page

t1 = threading.Thread(target=parse_1, args=[soup])
t2 = threading.Thread(target=parse_2, args=[soup])

t1.start()
t2.start()

t1.join()
t2.join()
