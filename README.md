# CNA-Web-Scraping
This repository contains a Python script for scraping the latest news articles from Channel NewsAsia's website. The script extracts article titles, categories, and timestamps, and then generates a bar chart, a word cloud, and an Excel file with this data.

## Overview

The script uses `requests` for fetching webpage content, `BeautifulSoup` for parsing HTML, and `pandas`, `matplotlib.pyplot`, and `WordCloud` for data processing and visualization. The output includes a visualization of the number of articles by category, a word cloud of the article titles, and an Excel file with the extracted data.

## Installation

To run this script, you need Python installed on your system along with the following libraries:
- BeautifulSoup
- pandas
- matplotlib
- wordcloud
- requests

## Project Setup
Install the required packages by running the following command in your terminal:
```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository to your local machine.
2. Navigate to the cloned directory.
3. Run the script using Python:


The script will create an `output` directory within the project folder containing the generated bar chart (`articles_by_category.png`), word cloud (`titles_wordcloud.png`), and Excel file (`CNA_latest_news.xlsx`).

## Structure

- `main.py`: The main Python script for scraping news articles.
- `output`: Folder containing the generated visualizations and Excel file.

## License

This project is open-sourced under the [MIT License](LICENSE).

