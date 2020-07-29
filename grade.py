"""
created by nakayama
github: vnakayama
e-mail: nakayama@ufrj.br

to-do: add category automatically, append ACC and others, declare variables and then append
"""

############# imports
import re
import scrapy
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

############# code

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
# driver.get(url)
disciplinas = open('disciplinas2.txt','w')

astro = [
    'https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/761658BA-92A4-F79F-6268-CA716A32D813.html',
    'https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/7AC10A59-92A4-F79B-1E8E-D192798C6B4B.html'
    ]

# discs = list()
driver.get('https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/7AC10A59-92A4-F79B-1E8E-D192798C6B4B.html')

duracao = int(driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table/tbody/tr[3]/td[2]').text[0])
for i in range(2,duracao*2,2):
    periodo = driver.find_element_by_xpath('/html/body/table/tbody/tr['+str(i)+']/td/table/tbody/tr/td/table/tbody[2]')
    semester = i/2
    disciplinas1 = periodo.find_elements_by_class_name('tableBodyBlue1')
    disciplinas2 = periodo.find_elements_by_class_name('tableBodyBlue2')
    for disciplina in disciplinas1:
        try:
            disc = '{name:"'+str(disciplina.find_elements_by_tag_name('td')[1].text)+'",credits:'+str(disciplina.find_elements_by_tag_name('td')[2].text)+',code:"'+str(disciplina.find_elements_by_tag_name('td')[0].text)+'",semester:'+str(i/2)+',workload:'+str(int(disciplina.find_elements_by_tag_name('td')[3].text)+int(disciplina.find_elements_by_tag_name('td')[4].text)+int(disciplina.find_elements_by_tag_name('td')[5].text))+',requirements:'+str([disciplina.find_elements_by_tag_name('td')[6].text])+'}'
            disciplinas.write(disc+','+'\n')
        except:
            pass
    for disciplina in disciplinas2:
        try:
            disc = '{name:"'+str(disciplina.find_elements_by_tag_name('td')[1].text)+'",credits:'+str(disciplina.find_elements_by_tag_name('td')[2].text)+',code:"'+str(disciplina.find_elements_by_tag_name('td')[0].text)+'",semester:'+str(i/2)+',workload:'+str(int(disciplina.find_elements_by_tag_name('td')[3].text)+int(disciplina.find_elements_by_tag_name('td')[4].text)+int(disciplina.find_elements_by_tag_name('td')[5].text))+',requirements:'+str([disciplina.find_elements_by_tag_name('td')[6].text])+'}'
            disciplinas.write(disc+','+'\n')
        except:
            pass

driver.close()