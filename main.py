import requests
import logging as log
from bs4 import BeautifulSoup


log.basicConfig(level=log.INFO)
#HTML_PARSER= BeautifulSoup(html_doc, 'html.parser')

def is_downloadable_pdf(url):
    """
    Does the url contain a downloadable pdf
    """
    h = requests.head(url)
    header = h.headers
    content_type = header.get('content-type')
    if 'pdf' in content_type.lower():
        return True  
    return False

def getURLContent(url):
    response=requests.get(url)
    if response.status_code == requests.status_codes.codes.ok:
        return response.content
    else:
        log.error(f"Unable to get content of the following URL:{url}.The requests return a status code of {response.status_code}")
        

def downloadLink(url_source,url,destination="./"):
    log.info(f"Attempting to download:{url}")
    if not('http' in url):
       url=url_source+url
        
    if(is_downloadable_pdf(url)):
        contents=getURLContent(url)
        filename=url.split('/')[-1]
        with open(destination+filename,"wb") as f:
            f.write(contents)

    else:
        log.info("{url} is not a downloadable pdf")
def main():
    urls=[]
    url="http://people.scs.carleton.ca/~lanthier/teaching/COMP2401/notes.html"
    urlContent= getURLContent(url)

    if(urlContent):
        PARSER=BeautifulSoup(urlContent, 'html.parser')
        info=f""
        links=PARSER.find_all('a')
        log.info(f"The following url:{url} has the following links:")
        for link in links:
            log.info(link.get('href'))

        for link in links:
            downloadLink(url,link.get('href'))
        



if __name__ == "__main__":
    main()
