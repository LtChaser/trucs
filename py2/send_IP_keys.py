# usage: python send_IP_keys.py Command_To_Send
import socket
import sys
from urllib2 import Request, urlopen
import json
import time
import logging
import os

logging_done = False



key_dict = {
    'ok':       '\xe0\x01',
    'power': '\xe0\x00',
    'channel+': '\xe0\x06',
    'channel-': '\xe0\x07',
    'stop': '\xe4\x02',
    'forward': '\xe4\x05',
    'rewind': '\xe4\x07',
    'play': '\xe4\x00',
    'record': '\xe4\x03',
    'previous linear': '\xef\x20',
    'red': '\xe2\x00',
    'green': '\xe2\x01',
    'yellow': '\xe2\x02',
    'blue': '\xe2\x03',
    'up': '\xe1\x00',
    'down': '\xe1\x01',
    'left': '\xe1\x02',
    'right': '\xe1\x03',
    'menu': '\xef\x00',
    'back': '\xe0\x02',
    'help': '\xe0\x09',
    'info': '\xe0\x0e',
    'myrecordings': '\xef\x29',
    'tvguide': '\xe0\x0b',
    'ondemand': '\xef\x28',
    'text': '\xe0\x0f',
    '0':'\xe3\x00',
    '1': '\xe3\x01',
    '2': '\xe3\x02',
    '3': '\xe3\x03',
    '4': '\xe3\x04',
    '5': '\xe3\x05',
    '6': '\xe3\x06',
    '7': '\xe3\x07',
    '8': '\xe3\x08',
    '9': '\xe3\x09',
	'a': '\x00\x41',
	'b': '\x00\x42',
	'c': '\x00\x43',
	'd': '\x00\x44',
	'e': '\x00\x45',
	'f': '\x00\x46',
	'g': '\x00\x47',
	'h': '\x00\x48',
	'i': '\x00\x49',
	'j': '\x00\x4a',
	'k': '\x00\x4b',
	'l': '\x00\x4c',
	'm': '\x00\x4d',
	'n': '\x00\x4e',
	'o': '\x00\x4f',
	'p': '\x00\x50',
	'q': '\x00\x51',
	'r': '\x00\x52',
	's': '\x00\x53',
	't': '\x00\x54',
	'u': '\x00\x55',
	'v': '\x00\x56',
	'w': '\x00\x57',
	'x': '\x00\x58',
	'y': '\x00\x59',
	'z': '\x00\x5a',
    'A': '\x00\x61',
	'B': '\x00\x62',
	'C': '\x00\x63',
	'D': '\x00\x64',
	'E': '\x00\x65',
	'F': '\x00\x66',
	'G': '\x00\x67',
	'H': '\x00\x68',
	'I': '\x00\x69',
	'J': '\x00\x6a',
	'K': '\x00\x6b',
	'L': '\x00\x6c',
	'M': '\x00\x6d',
	'N': '\x00\x6e',
	'O': '\x00\x6f',
	'P': '\x00\x70',
	'Q': '\x00\x71',
	'R': '\x00\x72',
	'S': '\x00\x73',
	'T': '\x00\x74',
	'U': '\x00\x75',
	'V': '\x00\x76',
	'W': '\x00\x77',
	'X': '\x00\x78',
	'Y': '\x00\x79',
	'Z': '\x00\x7a',
    'space': '\x00\x20'
    
}

def send_one_key(s, key) :

    kc = key_dict.get(key)
    if kc is None :
      return False

    logging.debug("Sending keyCode: %s", kc.encode('hex'))
    
    mt = '\x04' # message type for keyEvent
    kd = '\x01' # key pressed
    ku = '\x00' # key released
    p = '\x00\x00\x00\x00' # padding
    code = True
    try :
      s.send( mt + kd + p + kc)
      s.send( mt + ku + p + kc)
    except: 
      code = False
    return code

def init_connect(host) :

   try :
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((host, 5900))
       # receive and echo the version: "RFB 003.008\n"
       answer = s.recv(12)
       logging.debug("Version: %s", answer)
       s.send(answer)

       # receive number of schemes + the security schemes: '\x01\x01'
       answer = s.recv(8)
       logging.debug("Security scheme: %s", answer.encode('hex'))
       s.send('\x01')  # None security

       # receive security result: '\x00\x00\x00\x00'
       answer = s.recv(4)
       logging.debug("Security result: %s", answer.encode('hex'))
       # Send client initialisation shared flag
       s.send('\x01')  # shared

       # receive Server intitializaton: display settings (not used on Horizon)
       answer = s.recv(24)
       logging.debug(answer.encode('hex'))
       return s

   except :
       logging.exception("Error to init_connect")
       return None

def end_connect(s) :
    try: 
        close(s)
    except:
        pass
    return None

x = 1
    
stbip = "192.168.192.2"
while x == 1:
	key = raw_input(">")
	s = init_connect(stbip)
	send_one_key(s, key)
	end_connect(s)
	if key == "quit":
		x = 0