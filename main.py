import configparser
import json
import os
import platform
import subprocess
import time

import requests


class ToontownLauncher:

    def __init__(self, directory):

        self.directory = directory
        self.api_url = 'https://www.toontownrewritten.com/api/login?format=json'

    def connect(self, **data):
        print(data)

        post = requests.post(
            self.api_url,
            data=data,
            headers={'Content-type': 'application/x-www-form-urlencoded'},
        )

        response = post.json()

        success = response.get('success', 'false')

        if success == 'true':
            print('True.')
            print(response)
            cookie = response.get('cookie', 'CookieNotFound')
            game_server = response.get('gameserver', 'ServerNotFound')
            self._launch_game(cookie, game_server)

        elif success == 'false':
            print('False.')
            pass

        elif success == 'partial':
            print('Partial.')
            pass

        elif success == 'delayed':
            print('Delayed.')
            queue_token = response.get('queueToken')
            position = response.get('position')
            print(f'You are currently queued in position {position}.')
            time.sleep(3)
            self.connect(queueToken=queue_token)

    def _launch_game(self, play_cookie, game_server):

        os.environ['TTR_PLAYCOOKIE'] = play_cookie
        os.environ['TTR_GAMESERVER'] = game_server

        # engine = os.path.join(self.directory, 'TTREngine.exe')
        # os.system(f'"{engine}"')
        os.chdir(self.directory)
        subprocess.Popen(args="TTREngine.exe", creationflags=0x08000000)
        print('Successfully connected')
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
    launcher1.connect(username=username1, password=password1)

    launcher2 = ToontownLauncher(toontown_directory)
    launcher2.connect(username=username2, password=password2)
