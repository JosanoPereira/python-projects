# import library
# from selenium import webdriver
# import time
# from webdriver_manager import driver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
#
# # to sail to the whatsapp web
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://web.whatsapp.com/')
# time.sleep(10)
#
# # whos contacts/ wich message?
# contacts = ['Murky Wolf', 'Mamã', 'Pai']
# mensagem = 'Olá, sou o Programador Josano! Se recebeu essa mensagem é pq o meu algoritmo de automação funcionou!'
#
#
# # contacts/groups
# def research_contacts(contacto):
#     campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
#     time.sleep(3)
#     campo_pesquisa.click()
#     campo_pesquisa.send_keys(contacto)
#     campo_pesquisa.send_keys(Keys.ENTER)
#
#
# def send_message(mensagem):
#     campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
#     campo_mensagem[1].click()
#     campo_mensagem[1].send_keys(mensagem)
#     campo_mensagem[1].send_keys(Keys.ENTER)
#     time.sleep(3)
#
#
# for contacto in contacts:
#     research_contacts(contacto)
#     send_message(mensagem)
# research field 'copyable-text selectable-text'
# private message field 'copyable-text selectable-text'
#  send menssage to contacts or groups
