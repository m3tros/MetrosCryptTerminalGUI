import os
import sys
import cryptocode
import webbrowser
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.styles import Style


__version__ = 1.1

def message(self):
    message_dialog(title='MetrosCryptTerminalGUI {}'.format(__version__), text=text).run()
        

class main:

    terminal_work = True

    def __init__(self):
        super().__init__()
        while self.terminal_work == True:
            try:
                self.menu_init()
                self.command_init()
            except:
                pass

    def menu_init(self):
        self.main_menu = radiolist_dialog(
            title='Select an action',
            text='What are you going to do?',
            values=[
                ('encrypt_file', 'Encrypt the file...'),
                ('decrypt_file', 'Decrypt the file...\n'),
                ('echo_encrypt_file',
                 'Take the value encrypt from the file and output...'),
                ('echo_decrypt_file',
                 'Take the value decrypt from the file and output...\n'),
                ('view_spawn_algorithm_pypi', 'Open PyPi encryption algorithm...\n'),
                ('view_spawn_program', 'View the help of the program...'),
                ('view_spawn_website', 'Open the developer\'s website...'),
                ('view_spawn_github',
                 'Open the developer\'s github (John-MetrosSoftware)...\n'),
                ('exit', 'Exit the program.')
            ]
        ).run()

    def command_init(self):
        if self.main_menu == 'encrypt_file':
            self.file_encrypt_decrypt(action='encrypt_file')
        if self.main_menu == 'decrypt_file':
            self.file_encrypt_decrypt(action='decrypt_file')
        if self.main_menu == 'echo_encrypt_file':
            self.file_encrypt_decrypt(action='echo_encrypt_file')
        if self.main_menu == 'echo_decrypt_file':
            self.file_encrypt_decrypt(action='echo_decrypt_file')
        if self.main_menu == 'view_spawn_algorithm_pypi':
            webbrowser.open_new_tab('https://pypi.org/project/cryptocode/')
        if self.main_menu == 'view_spawn_website':
            webbrowser.open_new_tab('http://metros-software.ru')
        if self.main_menu == 'view_spawn_github':
            webbrowser.open_new_tab('https://github.com/John-MetrosSoftware/')
        if self.main_menu == 'view_spawn_program':
            webbrowser.open_new_tab(
                'https://github.com/John-MetrosSoftware/MetrosCryptTerminalGUI')
        if self.main_menu == 'exit' or self.main_menu == None:
            self.terminal_work = False

    def file_encrypt_decrypt(self, action):
        if action == 'encrypt_file':
            text_input = 'Enter the password to encrypt the file.'
        if action == 'decrypt_file':
            text_input = 'Enter the password to decrypt the file.'
        if action == 'echo_encrypt_file':
            text_input = 'Enter the password to output the contents of the encrypted file.'
        if action == 'echo_decrypt_file':
            text_input = 'Enter the password to output the contents of the decrypted file.'
        file_name = str(input_dialog(
            title='Enter the path to the file.', text='File:').run())
        if file_name == 'None':
            return
        if os.path.isfile(file_name) == False:
            self.message('Could not find the file ({}).'.format(file_name))
        elif os.path.isfile(file_name) == True:
            password = str(input_dialog(title=text_input,
                           text='Password:', password=True).run())
            if action == 'encrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_encrypt = cryptocode.encrypt(
                        file_name_open, password)
                    if result_encrypt != False:
                        file = open(file_name, 'w+')
                        file.write(str(result_encrypt))
                        file.close()
                    else:
                        self.message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    self.message(str(error))
                    return
                else:
                    self.message('The file has been successfully encrypted!')
                    return
            if action == 'decrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_decrypt = cryptocode.decrypt(
                        file_name_open, password)
                    if result_decrypt != False:
                        file = open(file_name, 'w+')
                        file.write(str(result_decrypt))
                        file.close()
                    else:
                        self.message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    self.message(str(error))
                    return
                else:
                    self.message('The file has been successfully decrypted!')
                    return
            if action == 'echo_encrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_encrypt = cryptocode.encrypt(
                        file_name_open, password)
                    print(result_encrypt)
                    if result_encrypt != False:
                        self.message(result_encrypt+'\n\n'+'_' *
                                     50+'\nEncrypted file: '+file_name)
                    else:
                        self.message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    self.message(str(error))
                    return
            if action == 'echo_decrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_decrypt = cryptocode.decrypt(
                        file_name_open, password)
                    if result_decrypt != False:
                        self.message(result_decrypt+'\n\n'+'_' *
                                     50+'\nDecrypted file: '+file_name)
                    else:
                        self.message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    self.message(str(error))
                    return


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        errors('Unknown error: {}'.format(str(error)))
