import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whats_response import response_message

mouse = Controller()

class Bot_Whatsapp:

    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.mensagem = ''
        self.ultima_mensagem = ''

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print(f'Erro em (nav_green_dot): {e}')

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print(f'Erro em (nav_input_box): {e}')

    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, -50, duration=self.speed)
        except Exception as e:
            print(f'Erro em (nav_message): {e}')

    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.mensagem = pc.paste()
        print(self.mensagem)

    def send_message(self):
        try:
            if self.mensagem != self.ultima_mensagem:
                bot_response = response_message(self.mensagem)
                print(bot_response)
                pt.typewrite(bot_response, interval=.1)
                self.ultima_mensagem = self.mensagem
            else:
                print('no new messages...')
        except Exception as e:
            print(f'Erro em (send_message): {e}')


bot = Bot_Whatsapp(speed=.5, click_speed=.3)
sleep(2)
bot.get_message()

