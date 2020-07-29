"""
created by nakayama
github: vnakayama
e-mail: nakayama@ufrj.br
"""
## Standard Library
import re

## Third-Party
import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

############# code

URL = 'https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/'
