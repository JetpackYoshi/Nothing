"""
nothing.py
==========

Honestly. This is truly nothing.
"""

import logging

logger = logging.getLogger(__name__)
special = logging.getLogger('special')

class Nothing:
    """
    Does nothing

    Parameters
    ----------
    nothing
        nothing.

    """
    def __init__(self,nothing):
        pass
    def nothing(self):
        pass

if __name__ == '__main__':
    nothing = Nothing()