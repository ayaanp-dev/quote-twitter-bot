import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://www.curatedquotes.com/inspirational-quotes/")
soup = bs.BeautifulSoup(source, "lxml")

print(soup.title)