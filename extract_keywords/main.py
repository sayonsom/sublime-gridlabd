from bs4 import BeautifulSoup
import requests

# Save the HTML page of interest, and pass the HTML File address here



r  = requests.get("http://gridlab-d.shoutwiki.com/wiki/Power_Flow_User_Guide")
data = r.text

soup = BeautifulSoup(data, features="lxml")


tables = soup.findAll("table")
syntax_list = []

for t in tables:
    count = 0
    for row in t.tbody.findAll('tr'):
        if count == 0:
            count += 1
            continue

        else:
            x = str(row.find('td'))
            x = x.replace("<td>","").replace("\n</td>","").replace(",","").replace("<td align=\"center\">","")
            syntax_list.append(x)
    
syntax_string = ""

for s in syntax_list:
    syntax_string += s + "|"

print(syntax_string)
