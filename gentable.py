#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import product
import hashlib
import time

def computeMD5hash(string):
  m = hashlib.md5()
  m.update(string.encode('utf-8'))
  return m.hexdigest()

try:
  print('---------------------------------------------------')
  #md5hash = input('MD5 hash to Crack: ')
  maxlen = int(input('Max String Length: ')) + 1
  print('---------------------------------------------------')

  chr = '''1): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890
2): abcdefghijklnmopqrstuvwxyz1234567890
3): ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
4): 1234567890
5): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz
6): ABCDEFGHIJKLMNOPQRSTUVWXYZ
7): abcdefghijklnmopqrstuvwxyz
8): Custom'''
		
  print(chr)
  print('---------------------------------------------------')
  char_num = int(input('Enter chars option number: '))

  if char_num == 1:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890'
  elif char_num == 2:
    chars = 'abcdefghijklnmopqrstuvwxyz1234567890'
  elif char_num == 3:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  elif char_num == 4:
    chars = '1234567890'
  elif char_num == 5:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz'
  elif char_num == 6:
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  elif char_num == 7:
    chars = 'abcdefghijklnmopqrstuvwxyz'
  elif char_num == 8:
    chars = input('Insert your custom list of chars: ')

  dic = input('Save dictionary (Y/N): ')
  if dic.lower() == 'y':
    name = input('Enter destination file name without extension: ') + '.txt'

  stop = 0
  found = 0
  lines = 0

  if dic.lower() == 'y':
    _file = open(name, 'w')

  tic = time.time()

  for length in range(1, maxlen):
    to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
      crypt = computeMD5hash(''.join(attempt))
      if dic.lower() == 'y':
          _file.write('{} = {}\n'.format(crypt, ''.join(attempt)))
          print('{} - {}'.format(''.join(attempt), crypt))
          lines += 1
    if stop == 1:
      break

  if dic.lower() == 'y':
    _file.close()
  toc = time.time()
  ttn = toc - tic

  print('Done! in {} seconds. With {} total hashes'.format(str(ttn), str(lines)))
  if found == 0:
    #print('Hash not Cracked :(')
    print('---------------------------------------------------')
except KeyboardInterrupt:
  print('\n Stopped at line: {}'.format(str(lines)))
