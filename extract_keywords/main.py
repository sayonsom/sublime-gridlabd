from bs4 import BeautifulSoup


# Save the HTML page of interest, and pass the HTML File address here
url = "C:\\Users\\CHANDS3\\Desktop\\Power Flow User Guide - GridLAB-D Wiki.html"
soup = BeautifulSoup(url.read())


xx = soup.find_all("pre")

print(xx)

lore