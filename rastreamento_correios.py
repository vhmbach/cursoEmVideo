import requests
from bs4 import BeautifulSoup

req = requests.post('https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?track={codigo}')