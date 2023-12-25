import pandas as pd
import requests
from bs4 import BeautifulSoup
import regex as re

# Headers mimic the profile and activity of real users
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko)'
                         'Chrome/80.0.3987.162 Safari/537.36'}

webpage = requests.get('https://www.ambitionbox.com/list-of-companies', headers=headers).text

soup = BeautifulSoup(webpage, 'lxml')
# print(soup.prettify())

"""
print(soup.find_all('h1')[0].text)  # h[n], n = size of text

print(len(soup.find_all('h1')))  # Number of h1 tags

for i in soup.find_all('h2'):
    print(i.text.strip())

print("P tags:")
for i in soup.find_all('p'):
    print(i.text.strip())
"""

# Analysing each company profile on the webpage
company = soup.find_all('div', class_='companyCardWrapper')
print(company)  # Visualise the company sections
print(len(company))  # Prints number of companies on the page
name = []
rating = []
reviews = []
ownership = []
for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('span', class_='companyCardWrapper__companyRatingValue').text.strip())
    reviews.append(i.find('span', class_='companyCardWrapper__ActionCount').text.strip())

    # Extract ownership information
    ownership_text = i.find('span', class_='companyCardWrapper__interLinking').text.strip()
    ownership_match = re.search(r'\b(Public|Private)\b', ownership_text)
    if ownership_match:
        ownership.append(ownership_match.group(0))
    else:
        ownership.append('Private')

data = {'Name': name, 'Rating': rating, 'Reviews': reviews, 'Ownership': ownership}
df = pd.DataFrame(data)
print(df)
