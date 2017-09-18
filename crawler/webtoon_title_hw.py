from bs4 import BeautifulSoup

f = open('text.txt', 'rt')

source = f.read()
soup = BeautifulSoup(source, 'lxml')

title_list = soup.findAll('td', attrs={'class':'title'})

for x in title_list:
    print(x.find('a').text)
    
