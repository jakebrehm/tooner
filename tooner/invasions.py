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
    Toontown Rewritten API and get information about invasions that are 
    currently happening.

    This class simply communicates with the Toontown Rewritten API to 
    get the latest invasion information. It also does a very basic 
    cleaning of the API's response.
    
    Properties:
        invasions:
            Returns a dictionary of current Toontown invasions, where 
            the key is the district that is being invaded and the value 
            is the cog that is invading that district.
        cogs:
            Returns a list of cogs that are currently invading 
            Toontown.
        districts:
            Returns a list of districts that are currently being 
            invaded.
    '''

    def __init__(self):
        '''Please see help(InvasionTracker) for more info.'''

        self.api_url = 'https://www.toontownrewritten.com/api/invasions'
    
    @property
    def invasions(self):
        '''A simple wrapper around the get_invasions method.'''

        return self.get_invasions()
    
    @property
    def cogs(self):
        '''Returns a list of currently-invading cogs.'''

        cogs = [invasion['type'] for invasion in self._invasions.values()]
        cogs = [cog.replace('\x03', '') for cog in cogs]
        return cogs
    
    @property
    def districts(self):
        '''Returns a list of currently-invaded districts.'''

        districts = list(self._invasions.keys())
        return districts

    def get_invasions(self):
        '''Returns information about currently invading cogs.'''

        return {k: self._clean(v['type']) for k, v in self._invasions.items()}

    def _make_request(self):
        '''Makes a get request to the Toontown Rewritten API.
        
        Returns the raw json response from the API, which includes 
        information about Toontown's current invasions.'''

        # Make a get request to the Toontown Rewritten API
        request = requests.get(self.api_url)
        # Return the json data from the response
        return request.json()
    
    def _clean(self, string):
        '''Removes undesired information/characters from a string.
        
        For some cogs, some byte artifacts (such as \x03) are still 
        included in the string. These aren't typically desired, so they 
        are replaced with an empty string.

        Args:
            string (str):
                The string to clean.
        '''

        return string.replace('\x03', '')

    @property
    def _invasions(self):
        '''Returns relevant information from the API's json response.'''

        return self._make_request()['invasions']
