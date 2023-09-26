import pyautogui
import time
#Este arquivo serve pra descobrir "as coordenadas" do seu mouse
time.sleep(5)#tempo definido para você colocar o mouse sobre as opções
print(pyautogui.position()) #primeiro você deixa o mouse sobre o botão de desligar o pc, depois você executa novamente o arquivo e deixa sobre a opçâo desligar, ai após receber as "coordenadas", retorne ao arquivo principal
