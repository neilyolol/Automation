#!/usr/local/bin/python

from pexpect import pxssh
import getpass

try:
	s = pxssh.pxssh()
	hostname = input('hostname: ')
	username = input('username: ')
	password = getpass.getpass('please input password: ')
	s.login(hostname,username,password)
	s.sendline('uptime')
	s.prompt()
	print(s.before)
	s.logout()
except pxssh.ExceptionPxssh as err:
	print(err)
