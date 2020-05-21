# -*- coding: utf-8 -*-

'''
tooner.launcher module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions and classes related to communicating with the Toontown
Rewritten API, logging in, and opening the launcher.
'''

import configparser
import os
import platform
import subprocess
import time

import requests


class ToontownLauncher:
    '''Uses the given login information to communicate with the
    Toontown Rewritten API in an attempt to log in and launch the game.
    
    Args:
        directory (str):
            The directory of your Toontown Rewritten installation.
    
    Kwargs:
        attempts (int) [5]:
            The maximum number of attempts to connect before giving up.
            Accepts a None value to try infinitely, but this is not
            recommended.
        debug (bool) [True]:
            Whether to write information to the console detailing
            communication with the API.
    '''

    def __init__(self, directory, attempts=5, debug=False):
        '''Please see help(ToontownLauncher) for more info.'''

        self.directory = directory
        self.api_url = 'https://www.toontownrewritten.com/api/login?format=json'

        self._attempts = 0
        self.maximum_attempts = attempts

        self._debug = debug
        self._stdout = None if debug else subprocess.DEVNULL

    def play(self, **data):
        '''A more intuitively-named wrapper for the _connect method.'''

        self._connect(**data)

    def _message(self, message):
        '''Print a message to the console.'''

        if self._debug:
            print(message)

    def _connect(self, **data):
        '''Communicate with the Toontown Rewritten API in an attempt to
        connect and log in.
        
        Kwargs:
            username (str):
                The username of the Toontown Rewritten account.
            password (str):
                The password of the Toontown Rewritten account.
            appToken (str):
                The ToonGuard code generated by an authenticator app.
                Only required if ToonGuard is activated for the
                Toontown Rewritten account.
        '''

        # Increment attempts counter and stop if the maximum has been reached
        self._attempts += 1
        if self.maximum_attempts and self._attempts > self.maximum_attempts:
            self._message(
                'The maximum number of attempts has been reached. '
                'Please try again.'
            )
            return

        # If the connection request 
        app_token = data.pop('appToken', None)

        # Post a request and determine its success
        response = self._make_request(data)
        success = response.get('success', 'false')

        # If the connection was successful, proceed to launch the game
        if success == 'true':
            cookie = response.get('cookie', 'CookieNotFound')
            game_server = response.get('gameserver', 'ServerNotFound')
            self._message('Successful granted access.')
            self._launch_game(cookie, game_server)
        # If the success was partial, a ToonGuard code is required to log in
        elif success == 'partial':
            authorization_token = response.get('responseToken', None)
            if not app_token or not authorization_token:
                self._message('Something went wrong. Please try again.')
                return
            time.sleep(3)
            self._connect(appToken=app_token, authToken=authorization_token)
        # If success was delayed, the user was placed in a queue
        elif success == 'delayed':
            queue_token = response.get('queueToken', None)
            if not queue_token:
                self._message('Something went wrong. Please try again.')
                return
            position = response.get('position')
            self._message(f'You are currently queued in position {position}.')
            time.sleep(3)
            self._connect(queueToken=queue_token)
        # Otherwise, the connection has failed
        else:
            self._message(
                'Connection failed. Something went wrong, but maybe it was '
                'just your username and password.'
            )

    def _make_request(self, data):
        '''Communicates with the Toontown Rewritten API to post a
        request.
        
        Args:
            data (dict):
                The data to send with the request.    
        '''

        # Post a request to the Toontown Rewritten API
        post = requests.post(
            self.api_url,
            data=data,
            headers={'Content-type': 'application/x-www-form-urlencoded'},
        )
        # Return the json data from the response
        return post.json()

    def _launch_game(self, play_cookie, game_server):
        '''Use the given response credentials to open the luancher and
        log into the game.
        
        Args:
            play_cookie (str):
                The cookie key used to log in. Received from the
                Toontown Rewritten API.
            game_server (str):
                The gameserver key used to log in. Received from the
                Toontown Rewritten API.
        '''

        # Determine the user's operating system
        operating_system = platform.system()
        # Change to the Toontown Rewritten directory
        os.chdir(self.directory)

        # Set the enironmental variables including login information
        os.environ['TTR_PLAYCOOKIE'] = play_cookie
        os.environ['TTR_GAMESERVER'] = game_server

        # Start the Toontown Rewritten process
        if operating_system == 'Windows':
            subprocess.Popen(
                args="TTREngine.exe",
                stdout=self._stdout,
                creationflags=0x08000000,
            )
        elif operating_system == 'Linux':
            # TODO: Linux features are currently untested.
            subprocess.Popen(args="./TTREngine", stdout=self._stdout)
        elif operating_system == 'Darwin':
            subprocess.Popen(args='./Toontown Rewritten', stdout=self._stdout)
        else:
            self._message('Your operating system is not currently supported.')
    
        # Let the user know the connection was successful
        self._message('Successfully connected.')


class InvasionTracker:
    '''Pulls invasion information from the Toontown Rewritten API.
    
    Uses the given login information to communicate with the
    Toontown Rewritten API in an attempt to log in and launch the game.

    This class is essentially simply communicates with the Toontown 
    Rewritten API to get the latest invasion information. It also does 
    a very basic cleaning of the API's response.
    
    Kwargs:
        debug (bool) [True]:
            Whether to write information to the console detailing
            communication with the API.
    '''

    def __init__(self, debug=False):
        '''Please see help(InvasionTracker) for more info.'''

        self.api_url = 'https://www.toontownrewritten.com/api/invasions'

        self._debug = debug
    
    @property
    def cogs(self):
        invasions = self._make_request()['invasions']
        cogs = [invasion['type'] for invasion in invasions.values()]
        cogs = [cog.replace('\x03', '') for cog in cogs]
        return cogs
    
    @property
    def districts(self):
        invasions = self._make_request()['invasions']
        districts = list(invasions.keys())
        return districts

    def get_invasions(self):
        invasions = self._make_request()

        invasions = {k: v['type'] for k, v in invasions['invasions'].items()}
        invasions = {k: v.replace('\x03', '') for k, v in invasions.items()}

        return invasions

    def _make_request(self):
        '''Makes a get request to the Toontown Rewritten API.'''

        # Make a get request to the Toontown Rewritten API
        request = requests.get(self.api_url)
        # Return the json data from the response
        return request.json()

        


if __name__ == '__main__':
    tracker = InvasionTracker()
    print(tracker.get_invasions())
    print(tracker.cogs)
    print(tracker.districts)