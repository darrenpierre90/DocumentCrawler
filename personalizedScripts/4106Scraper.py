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
    log.info("This is the content type:"+content_type)
    try:
        
        if 'pdf' in content_type.lower():
            return True  
        elif 'ppt' in content_type.lower():
            return True 
    except:
        log.error("unable to parse" + url)
        return False
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
        
    if('pdf' in url or "html" in url or "png" in url):
        
        contents=getURLContent(url)
        filename=url.split('/')[-1]
        with open(destination+filename,"wb") as f:
            f.write(contents)

    else:
        log.info("{url} is not a downloadable pdf")

def isLectureNote(link):
    # Filter links that are only the notes
    noteString="AI"
    noteString2="Ch"
    if noteString in link and noteString2 in link.get('href'):
        return True

    else:
        return False

def main():

    url= 'https://people.scs.carleton.ca/~oommen/Courses/COMP4106Winter20/'
    urlContent= getURLContent(url)

    if(urlContent):
        PARSER=BeautifulSoup(urlContent, 'html.parser')
        info=f""
        links=PARSER.find_all('a',href=True)
        links=filter(isLectureNote,links)
        log.info(f"The following url:{url} has the following links:")
        for link in links:
            log.info(link.get('href'))

        
        destination="/home/darren/CU/4106/Lectures/"
        for link in links:
            downloadLink(url,link.get('href'),destination)
        



if __name__ == "__main__":
    main()
