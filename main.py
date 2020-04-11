import configparser
import json
import os
import platform
import subprocess
import time

import requests


class ToontownLauncher:

    def __init__(self, directory, attempts=5, console_output=True):

        self.directory = directory
        self.api_url = 'https://www.toontownrewritten.com/api/login?format=json'

        self._attempts = 0
        self.maximum_attempts = attempts

        self.console_output = console_output

    def play(self, **data):
        self._connect(**data)

    def _message(self, message):
        if self.console_output:
            print(message)

    def _connect(self, **data):

        self._attempts += 1
        if self._attempts > self.maximum_attempts:
            self._message(
                'The maximum number of attempts has been reached. '
                'Please try again.'
            )
            return


        app_token = data.pop('appToken', None)

        post = requests.post(
            self.api_url,
            data=data,
            headers={'Content-type': 'application/x-www-form-urlencoded'},
        )

        response = post.json()

        success = response.get('success', 'false')

        if success == 'true':
            cookie = response.get('cookie', 'CookieNotFound')
            game_server = response.get('gameserver', 'ServerNotFound')
            self._message('Successful granted access.')
            self._launch_game(cookie, game_server)

        elif success == 'partial':
            authorization_token = response.get('responseToken', None)
            if not app_token or not authorization_token:
                pass # TODO
            time.sleep(3)
            self._connect(appToken=app_token, authToken=authorization_token)

        elif success == 'delayed':
            queue_token = response.get('queueToken', None)
            if not queue_token:
                pass # TODO
            position = response.get('position')
            self._message(f'You are currently queued in position {position}.')
            time.sleep(3)
            self._connect(queueToken=queue_token)

        elif success == 'false':
            self._message(
                'Connection failed. '
                'Please check your username and password and try again.'
            )

    def _launch_game(self, play_cookie, game_server):

        operating_system = platform.system()

        os.environ['TTR_PLAYCOOKIE'] = play_cookie
        os.environ['TTR_GAMESERVER'] = game_server

        os.chdir(self.directory)

        if operating_system == 'Windows':
            subprocess.Popen(args="TTREngine.exe", creationflags=0x08000000)
        elif operating_system == 'Linux':
            pass # TODO
        elif operating_system == 'Darwin':
            pass # TODO
        else:
            pass # TODO
    
        self._message('Successfully connected.')
        time.sleep(5) 
        

if __name__ == '__main__':

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(r'config.ini')

    # Read the login information for the first toon
    username1 = config['Toon 1']['username']
    password1 = config['Toon 1']['password']
    # Read the login information for the second toon
    username2 = config['Toon 2']['username']
    password2 = config['Toon 2']['password']

    # Set the directory of the Toontown Rewritten engine
    toontown_directory = r'C:\Program Files (x86)\Toontown Rewritten'

    # Launch the game
    launcher1 = ToontownLauncher(toontown_directory)
    launcher1.play(username=username1, password=password1)

    # launcher2 = ToontownLauncher(toontown_directory)
    # launcher2.play(username=username2, password=password2)
