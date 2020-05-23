# -*- coding: utf-8 -*-

'''
tooner.invasions module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions and classes related to communicating with the Toontown
Rewritten API and tracking invasions.
'''

import requests


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