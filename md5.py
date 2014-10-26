#!/usr/bin/env python
# -*- coding: utf-8 -*-
#username | password
#---------+---------------------------------
#michael  | e10adc3949ba59abbe56e057f20f883e
#bob      | 878ef96e86145580c38c87f0410ad153
#alice    | 99b1c2188db85afee403b1536010c2c9

import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
	if calc_md5(password) == db[user]:
		return True
	else:
		return False

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password) 
	pswd_md5 = md5.hexdigest()
	return pswd_md5 

if __name__=='__main__':
	username = raw_input('Please input your username: ')
	password = raw_input('Please input your password: ')
	if login(username,password) == True:
		print 'login success'
	else:
		print 'wrong password'	
