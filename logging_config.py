#!/opt/local/bin/python
# -*- coding: utf-8 -*-

import datetime
import os

"""
Contains a Config class that generates a dictionary for the global logging configuration.
"""

class Config:
    def __init__(self):
        ## For Generating Logfiles ##
        self.file_date = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")  # Current date and time
        self.log_dir = './logs/{}'.format(self.file_date)  # Directory to save logs in
        os.makedirs(self.log_dir, exist_ok=True)

        self.config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'detailed': {
                    'class': 'logging.Formatter',
                    'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
                },
                'simple': {
                    'class': 'logging.Formatter',
                    'format': '%(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
                },
                'default': {
                    'class': 'logging.Formatter',
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    'datefmt': '%m/%d/%Y %H:%M:%S'
                },
                'history': {
                    'class': 'logging.Formatter',
                    'format': '%(asctime)s %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'default',
                },
                'mpfile': {
                    'class': 'logging.FileHandler',
                    'filename': '{}/mplog.log'.format(self.log_dir),
                    'mode': 'w',
                    'formatter': 'detailed'
                },
                'specialFile': {
                    'class': 'logging.FileHandler',
                    'filename': '{}/special.log'.format(self.log_dir),
                    'mode': 'w',
                    'formatter': 'history',
                },
            },
            'loggers': {
                'special': {
                    'handlers': ['specialFile'],
                    'level': 'DEBUG'
                }
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['console', 'mpfile']
            }
        }