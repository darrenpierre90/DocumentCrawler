# Document Crawler

Document crawler is a web scraper that is used to download documents from websites.It can be used for automation of downloading resources that are posted regularly from a site that you want later want to check out.
## Motivation
The motivation of this project was that I sometimes come across a website that has many interesting documents either in pdf or PowerPoint I want to get. But there's a lot and I don't want to waste time going one by one and downloading it all . Why not web scrape them. This was also an excuse to experiment with python Beautiful Soup library to see what it can do , experience web scraping first hand and find it's limitations.This code often serves as my basis for web scraping certain web sites.

## Installation

clone the repo and run the following command

```bash
pip install -r requirements.txt
```

## Usage
Copy main.py into a new file .Then edit the new file to meets your needs.You probably want to implement a filter function so that you exclude the links that you don't want . Also you want to insert the link or links that you want to scrape . Document Scrapter assumes that the links that you want are on the HTML page you've initially hand into the script.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
