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

# Message function to display messages and errors on the screen.
def message(text):
    message_dialog(title='MetrosCryptTerminalGUI {}'.format(__version__), text=text).run()

class main:
    '''
    The main class of the program. 
    Class content:  
      menu_init - main menu initialization function.
      command_init - function to process the selected menu item.
      file_encrypt_decrypt - the encryption or decryption algorithm function also includes echo_encrypt_file and echo_decrypt_file - these are 3, 4 menu items.
    '''
  
    def __init__(self):
        super().__init__()
        self.terminal_work = True
        while self.terminal_work == True:
            try:
                self.menu_init()
                self.command_init()
            except:
                pass
    
    # Initialization of the main menu.
    def menu_init(self):
        self.main_menu = radiolist_dialog(
            title='Select an action',
            text='What are you going to do?',
            values=[
                ('encrypt_file', '1. Encrypt the file...'),
                ('decrypt_file', '2. Decrypt the file...\n'),
                ('echo_encrypt_file',
                 '3. Take the value encrypt from the file and output...'),
                ('echo_decrypt_file',
                 '4. Take the value decrypt from the file and output...\n'),
                ('view_spawn_algorithm_pypi', '5. Open PyPi encryption algorithm...\n'),
                ('view_spawn_program', '6. View the help of the program...'),
                ('view_spawn_website', '7. Open the developer\'s website...'),
                ('view_spawn_github',
                 '8. Open the developer\'s github (John-MetrosSoftware)...\n'),
                ('exit', '0. Exit the program.')
            ]
        ).run()
    
    # Processing the selected menu item.
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
    
    # Encryption and decryption algorithm.
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
            message('Could not find the file ({}).'.format(file_name))
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
                        message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    message(str(error))
                    return
                else:
                    message('The file has been successfully encrypted!')
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
                        message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    message(str(error))
                    return
                else:
                    message('The file has been successfully decrypted!')
                    return
            if action == 'echo_encrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_encrypt = cryptocode.encrypt(
                        file_name_open, password)
                    print(result_encrypt)
                    if result_encrypt != False:
                        message(result_encrypt+'\n\n'+'_' *
                                     50+'\nEncrypted file: '+file_name)
                    else:
                        message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    message(str(error))
                    return
            if action == 'echo_decrypt_file':
                try:
                    file_name_open = open(
                        file_name, encoding='utf-8', errors='ignore').read()
                    result_decrypt = cryptocode.decrypt(
                        file_name_open, password)
                    if result_decrypt != False:
                        message(result_decrypt+'\n\n'+'_' *
                                     50+'\nDecrypted file: '+file_name)
                    else:
                        message(
                            'The file could not be opened. ({}). There may be an incorrect password.'.format(file_name))
                        return
                except Exception as error:
                    message(str(error))
                    return


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        message('Unknown error: {}'.format(str(error)))
