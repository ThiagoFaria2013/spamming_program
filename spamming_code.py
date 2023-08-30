import pyautogui as pag
import time

vezes_mandadas = int(0)

def localizacao():
    input('when you press enter, the program will count until 10, you have 10 seconds to put your mouse on the writing bar of wherever you want to spam a messege. please leave it there for 10 seconds so we can capture it:')

    time.sleep(10)
    posição = pag.position()
    return posição


def spama(posição, vezes_para_mandar, mensagem):
    pag.write(mensagem)
    pag.press('enter')


def definir_mensagem():
    mensagem = input('write the message that you want to spam:')
    return mensagem

def definir_vezes():
    vezes = int(input('write the number of times that you want to spam the message:')) - 1
    return vezes

mensagem = definir_mensagem()
vezes = definir_vezes()
posição = localizacao()

pag.click(posição)

while vezes_mandadas <= vezes:
    spama(posição,vezes_mandadas,mensagem)
    vezes_mandadas += 1