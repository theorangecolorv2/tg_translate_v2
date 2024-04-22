import translate_response
import pyperclip
import keyboard
import time
import pyautogui

class Translator:
    def __init__(self, source_lang=1, autodetect=True, target_lang=0, hotkey="ctrl+t", paste_res_to_buffer=True):
        self.source_lang = source_lang
        self.autodetect = autodetect
        self.target_lang = target_lang
        self.hotkey = hotkey
        self.paste_res_to_buffer = paste_res_to_buffer
        self.languages = ['ru', 'en', 'fr', 'es', '']

    def translate(self):
        if self.paste_res_to_buffer:  # поместить перевод в буффер обмена
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.1)
            q = pyperclip.paste()
            if self.autodetect:  # использовать автоопределение исходного языка
                pyperclip.copy(translate_response.translate_response(q, self.languages[self.target_lang]))
            else:
                pyperclip.copy(translate_response.translate_from_response(q, self.languages[self.source_lang], self.languages[self.target_lang]))
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')

    def change_source_lang(self, lang):
        self.source_lang = lang

    def change_target_lang(self, lang):
        self.target_lang = lang

    def change_autodetect(self, autodetect):
        self.autodetect = autodetect

    def change_paste_to_buffer(self, paste_to_buffer):
        self.paste_res_to_buffer = paste_to_buffer

