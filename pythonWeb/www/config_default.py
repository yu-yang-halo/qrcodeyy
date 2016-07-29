#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'qrcode'
    },
	'server':{
	    'ip':'192.168.2.119',
        'port':8080		
	},
    'session': {
        'secret': 'qrcode'
    }
}
