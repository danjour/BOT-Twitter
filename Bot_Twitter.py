# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:57:57 2020

@author:Eduardo D anjour
"""

from selenium import webdriver
import time

class Twitter:
    def __init__(self):
        #Abre o site do Twitter
        driver.get('https://twitter.com')
        #Pega o caminho via Xpath para o form do login de e-mail
        email_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input'
        #Pega o caminho via Xpath para o form do login da senha
        password_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input'
         #Pega o caminho via Xpath para o form do login do botão de entrar
        login_button_xpah='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div'
        self.email_element=driver.find_element_by_xpath(email_xpath)
        self.password_element=driver.find_element_by_xpath(password_xpath)
        self.login_button_element=driver.find_element_by_xpath(login_button_xpah)
        #Não coloquei todos os caminhos na mesma função pois ele procura por tudo de uma única vez, sendo necessário
        #nesse caso fazer por partes
            
 
    def logar(self):
        #Abre o form do usuario e digita o usuário previamente digitado 
        #é possível também fazer um for para que seja postado várias vezes com vários usuário
        #basta crIar uma list com usuários e senhas e fazer o loop
        self.email_element.send_keys('usuario')
        time.sleep(1)
        self.password_element.send_keys('senha')
        time.sleep(1)
        #Clica no botão
        self.login_button_element.click()

    def postar(self,msg):
        #Pega os caminhos
        post_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        tweetar_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div'
        post_element=driver.find_element_by_xpath(post_xpath)
        tweetar_element=driver.find_element_by_xpath(tweetar_xpath)
        #Abre o form e digita
        post_element.click()
        time.sleep(2)
        post_element.send_keys(msg)
        time.sleep(2)
        #Aqui ele realmente posta a mensagem
        tweetar_element.click()


msg=input("Qual mensagem deseja postar? ")
#Coloquei o driver como global pois estava tendo problemas com algumas funções
#É necessário portantol, nesse caso, deixar o chromedriver.exe na mesma pasta 
#do Py e é necessário verificar se a versão do arquivo é compativel com o navegador
#é possível mudar o navegador :D
driver=webdriver.Chrome(executable_path=r'./chromedriver.exe')
#Cria a instancia Twitter
bot=Twitter()
#Chama o logar
bot.logar()
#Chama o enviar mensagem
bot.postar(msg)











