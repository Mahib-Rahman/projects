import bs4
import urllib.request
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup
import csv


#the three trackers we're interrested in
a = "Google Firebase Analytics"
b = "Facebook Analytics"
c = "Flurry"


fields=["company Name", a, b, c]
with open(r'trackers.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

# file
# "company name" a, b , c


containers = []
for i in range(1,184667):
    my_url = f"https://reports.exodus-privacy.eu.org/en/reports/{i}/"
    
    #get page content from website
    try:
        uClient = uReq(my_url)
        page_html = uClient.read()
    except urllib.error.HTTPError as err:
        continue
    
    page_soup = soup(page_html, "html.parser")
    
    #get name of app (company name)
    company = str(page_soup.h1.text).replace(" ", "").replace("\n", "")
    
    #initialize row for the company
    append_row = [company, False, False, False]
    
    #go through trackers to check if the 3 target trackers are there
    containers = page_soup.findAll("p", {"class" : "mb-0"})
    for elm in containers:
        if elm.a.text == a:
            append_row[1] = True
        elif elm.a.text == b:
            append_row[2] = True
        elif elm.a.text == b:
            append_row[3] = True
    
    #append row
    #append it to file
    with open(r'trackers.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(append_row)
    

uClient.close()

#dict = {"Company Name" : company, a : list_a, b : list_b, c: list_c}
#df = pd.DataFrame(dict)
#df.to_csv("trackers.csv")
    