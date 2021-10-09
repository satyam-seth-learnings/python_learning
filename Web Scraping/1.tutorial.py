import bs4
import requests
# url="https://www.w3schools.com/"
# data=requests.get(url)
# soup=bs4.BeautifulSoup(data.text,'html.parser')
# # print(soup.prettify())
# # for para in soup.find_all('p'):
# #     print(para.text)
# for links in soup.find_all("a"):
#     link=links.get('href')
#     print("https://www.w3schools.com/"+link)
url2="https://www.youtube.com/channel/UCF7BExjT2zH_mmyqOB139Dg/playlists"
data=requests.get(url2)
soup=bs4.BeautifulSoup(data.text,'html.parser')
for link in soup.find_all('a'):
    link=link.get("href")
    if link[0:3]=="/wa":
        print("https://www.youtube.com"+link)