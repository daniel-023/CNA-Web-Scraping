import os.path
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Fetch webpage content
webpage = requests.get('https://www.channelnewsasia.com/latest-news').text

# Parse HTML content using Beautiful Soup
soup = BeautifulSoup(webpage, 'html.parser')
articles = soup.find_all('div', class_="media-object")

# Initialise lists to store article details
title = []
category = []
timestamp = []

# Loop through each article and extract details
for i in articles:
    # Extract and append article title
    title.append(i.find('h6').text.strip())

    # Extract and append article category
    category.append(i.find('p', class_='list-object__category').text.strip())

    # Extracting timestamp and converting into a readable format
    time_element = i.find('span', class_='list-object__timestamp')
    timestamp_value = time_element['data-lastupdated']
    readable_timestamp = datetime.fromtimestamp(int(timestamp_value))
    timestamp.append(readable_timestamp.strftime("%Y-%m-%d %H:%M:%S"))

# Create a DataFrame from the scraped data
data = {'Title': title, 'Category': category, 'Timestamp': timestamp}
df = pd.DataFrame(data)

# Convert 'Timestamp' column into datetime objects
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set a relative path
folder_name = 'output'
current_directory = os.path.dirname(__file__)  # Gets the directory where the script is located
path = os.path.join(current_directory, folder_name)

# Create directory if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

# Bar Chart: Number of Articles by Category
category_counts = df['Category'].value_counts()
plt.figure(figsize=(14, 10))
category_counts.plot(kind='bar', color='bisque')
plt.title('Number of Articles by Category')
plt.xlabel('Category')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45, ha='right')  # Rotate category names
plt.tight_layout(pad=5)
plt.savefig(os.path.join(path, 'articles_by_category.png'))

# WordCloud: Article Titles
all_titles = ' '.join(df['Title'])
wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(all_titles)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=5)
plt.savefig(os.path.join(path, 'titles_wordcloud'))

# Save the DataFrame to an Excel file
df.to_excel(os.path.join(path, 'CNA_latest_news.xlsx'), index=False)
