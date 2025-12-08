# Fetch a Web Page Title
from urllib import response
import requests
from bs4 import BeautifulSoup
html = "<html><head><title>Test Page</title></head><body></body></html>"
soup = BeautifulSoup(html, "html.parser")
print("Page Title:", soup.title.string)



# Extract All Links
import requests
from bs4 import BeautifulSoup
html = '<a href="page1.html">Page1</a> <a href="page2.html">Page2</a>'
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a", href=True):
    print(a["href"])




# Extract a Table into Python List
from bs4 import BeautifulSoup
html = """
<table>
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Alice</td><td>30</td></tr>
  <tr><td>Bob</td><td>25</td></tr>
</table>
"""
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")
for row in rows:
    cells = [td.text for td in row.find_all(["th", "td"])]
    print(cells)




# Automate Google Search Using Selenium


