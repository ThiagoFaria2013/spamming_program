import pyautogui as pag
import time

vezes_para_mandar = int(0)
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


mensagem = definir_mensagem()
posição = localizacao()

pag.click(posição)

while vezes_para_mandar <= 10:
    spama(posição,vezes_para_mandar,mensagem)
    vezes_para_mandar += 1