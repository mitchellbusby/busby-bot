import traceback
from bs4 import BeautifulSoup
import requests

def construct_payload(keywords):
    payload = "{pageIndex: 1,keyword:\"" + keywords + "\",method:\"0\",collection:\"\",refinements:\"\",datefrom:\"\",dateto:\"\",page:\"Books.aspx\", sort: \"1003\", bibid: \"\",c: 4,showall:0,stats:0,frm:\"\"}\n"
    
    return payload

def search(title):
    payload = construct_payload(title)

    url = "https://library.lmc.nsw.gov.au/montage/webmethods.aspx/GetTitlesAll"


    headers = {
        'accept': "application/json",
        'x-requested-with': "XMLHttpRequest",
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    text = response.json()

    resulting_xml = text["d"].replace('\r', '').replace('\n', '')
    # print(resulting_xml)

    ## TODO: beautifulsoup this thing
    ## TODO: Consider ISBN-filtering.
    soup = BeautifulSoup(resulting_xml, features='lxml')
    book = soup.html.body.newdataset.access
    if book == None:
        return None
    title = book.dds_title
    availability = int(book.countofitemsavailable.text)
    return BookResult(title, availability)

class BookResult:
    def __init__(self, title, availability):
        self.title = title
        self.availability = availability

    def is_book_available(self):
        return self.availability > 0

def is_book_available(title):
    try:
        result = search(title)
        if result == None:
            return False
        
        return result.is_book_available()
    except:
        # Print stack and return false
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    print(is_book_available('atlas shrugged'))