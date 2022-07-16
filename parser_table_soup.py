import requests 
from bs4 import BeautifulSoup

# content_table = """
# <table>
#     <thead>
#         <th>ID</th>
#         <th>Vendor</th>
#         <th>Product</th>
#     </thead>
#     <tr>
#         <td>1</td>
#         <td>Intel</td>
#         <td>Processor</td>
#     </tr>
#     <tr>
#         <td>2</td>
#         <td>AMD</td>
#         <td>GPU</td>
#     </tr>
#     <tr>
#         <td>3</td>
#         <td>Gigabyte</td>
#         <td>Mainboard</td>
#     </tr>
# </table>
# """

# soup = BeautifulSoup(content_table, 'html.parser')
# headers = {}
# rows = soup.find_all("tr")
# thead = soup.find("thead").find_all("th")

# for i in range(len(thead)):
#      headers[i] = thead[i].text.strip().lower()

# data = []

# for row in rows:
#      cells = row.find_all("td")

# item = {}

# for index in headers:
#      item[headers[index]] = cells[index].text
#      data.append(item)

# print(data)






### 2 вариант

response = requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_albums") 
soup = BeautifulSoup(response.content, 'html.parser') 

table = soup.find("table", class_="sortable")
output = []
for row in table.findAll("tr"):
    new_row = []
    for cell in row.findAll(["td", "th"]):
        for sup in cell.findAll('sup'):
            sup.extract()
        for collapsible in cell.findAll(
                class_="mw-collapsible-content"):
            collapsible.extract()
        new_row.append(cell.get_text().strip())
    output.append(new_row)

print(output)
# [ 
#     ['Artist', 'Album', 'Released', ...], 
#     ['Michael Jackson', 'Thriller', '1982', ...] 
# ]