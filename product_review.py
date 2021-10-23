#!/usr/bin/env python3

# Importing Modules
import requests
import bs4
import csv

# Requesting the webpage
hdrs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}

site = 'https://www.amazon.in/LG-24-inch-Monitor-Freesync-Borderless/dp/B08J5Y9ZSV/ref=sr_1_2?dchild=1&pf_rd_i=976392031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=fdf29120-98d8-40f7-810a-585fb8aa67c1&pf_rd_r=9NSA2WH49QR1TJ0815CK&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1634737622&smid=A14CZOWI0VEHLG&sr=8-2&th=1'
res = requests.get(site, headers=hdrs)

# Parsing the HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')

reviews = soup.find('div', id='reviewsMedley')

# Total rating of the product
glob_rating = reviews.find('span', attrs={'data-hook': 'rating-out-of-text'})
print('The product global rating is', glob_rating.string)

print('Star Ratings:')
star_reviews = reviews.find(id='histogramTable')

a = 5
for i in star_reviews.find_all('a')[2::3]:
    print(a, 'star rating -', str(i.string).strip())
    a -= 1

print('Now reading the reviews...')
review_list = reviews.find_all('div', attrs={'data-hook': 'review'})

# Opening the csv file
f = open('result.csv', mode='w', encoding='utf-8')
w = csv.writer(f, lineterminator='\n')

w.writerow(['Reviewer', 'Posted_date', 'Review_text'])

# Looping all the top reviews and accessing them
for i in review_list:
    name = i.find('span', attrs={'class': 'a-profile-name'})
    date = i.find('span', attrs={'class': 'review-date'})
    body = i.find('span', attrs={'data-hook': 'review-body'})

    # Cleaning the review body text
    while True:
        try:
            body.br.unwrap()
        except AttributeError:
            break
    b = str(body.span)
    b = b.removeprefix('<span>')
    b = b.removesuffix('</span>')
    b = b.strip()

    # Print the data
    # print('Name:', name.string)
    # print('Date:', date.string[21:])
    # print('Body:', b)
    # print('-' * 100)

    # Write data in the csv file
    w.writerow([name.string, date.string[21:], b])

f.close()

print('Data saved in result.csv...')
