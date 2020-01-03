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
        
    if('pdf' in url):
        destination='4601/'
        contents=getURLContent(url)
        filename=url.split('/')[-1]
        with open(destination+filename,"wb") as f:
            f.write(contents)

    else:
        log.info("{url} is not a downloadable pdf")


def filterLinks(link):
    if ('/wiki/index.php/Operating_Systems_2019F_Lecture_' in link.get('href')):
        return True
    else:
        False
def main():
    
    def filterLinks(link):
        if ('/wiki/index.php/Operating_Systems_2019F_Lecture_' in link.get('href')):
            return True
        else:
            False
    urls=['sikaman.dyndns.org:8888/courses/4601/index.html','http://people.scs.carleton.ca/~jeanpier/4004F19/','https://web.stanford.edu/class/cs276/']
    url="http://lass.cs.umass.edu/~shenoy/courses/377/lectures.html"
    url='https://homeostasis.scs.carleton.ca/wiki/index.php/Operating_Systems_(Fall_2019)'
    urlContent= getURLContent(url)

    if(urlContent):
        PARSER=BeautifulSoup(urlContent, 'html.parser')
        info=f""
        links=PARSER.find_all('a', href=True)
        log.info(f"The following url:{url} has the following links:")
        for link in links:
            if ('/wiki/index.php/Operating_Systems_2019F_Lecture_' in link.get('href')):
                log.info(link.get('href'))

        filterLinks=filter(filterLinks,links)
        for link in filterLinks:
            
            link=link.get('href')
            log.info("https://https://homeostasis.scs.carleton.ca/"+str(link))

            PARSER2=BeautifulSoup(getURLContent("https://homeostasis.scs.carleton.ca"+link), 'html.parser')
            log.info(PARSER2.find('pre'))
            fileContents=PARSER2.find('pre')
            fileNameIndex=link.index('Operating_Systems_2019F_Lecture_')
            fileName=link[fileNameIndex:] + ".txt"
            with open(fileName,'w') as lectureNotes:
                lectureNotes.write(str(fileContents))
            
     
        



if __name__ == "__main__":
    main()
