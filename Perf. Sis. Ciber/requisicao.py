import wget
import requests

req = requests.Request('GET', 'https://bibliotecaelfica.org/download/o-senhor-dos-aneis-a-sociedade-do-anel-j-r-r-tolkienumfiangla3s61ddmzcjlgw8z/')


wget.download(req, "livro baixado.txt")

