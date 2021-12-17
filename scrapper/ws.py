from bs4 import BeautifulSoup
import requests

#passando endereço para o objeto e chamando a requisição
site = requests.get("https://www.climatempo.com.br/").content

#objeto site recebendo o conteudo da requisição
soup = BeautifulSoup(site, 'html.parser')

#baixando o html do site convertendo em string e imprimindo
#print(soup.prettify())

temperatura = soup.find("p", class_="-gray _flex _align-center")

print(soup.find('admin'))