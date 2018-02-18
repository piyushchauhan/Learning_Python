from distutils.core import setup
import py2exe

setup(console=['collatz sequence.py'], requires=['pyperclip', 'pyperclip', 'openpyxl', 'requests', 'bs4', 'pyautogui',
                                                 'PIL'])
