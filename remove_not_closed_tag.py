from bs4 import BeautifulSoup

codeblock = '<strong>Good</strong> Some text and bad closed strong </strong> Some text and bad open strong PROBLEM HERE <strong> Some text <h2>Some</h2> or <h3>Some</h3> <p>Some Some text <strong>Good2</strong></p>'

soup = BeautifulSoup(codeblock, "html.parser")
# pretty = soup.prettify()
for item in soup.find_all('strong'):
    if item.findChild():
        item.unwrap()
print(soup)