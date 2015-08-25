#!/usr/bin/env python

import argparse
import ConfigParser
import os
import sys

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
Create a push
'''

def main():
	#  Argument Parser
	parser = argparse.ArgumentParser(description='Create a pushbullet message')

	# Key
	parser.add_argument('-t','--title',dest='title', help='Your pushbullet title', default="CLI")
	parser.add_argument('-m','--message',dest='message', help='Your pushbullet message', default="You got a CLI push")
	
	# Parse arguments
	args = parser.parse_args()
	title = args.title
	message = args.message

	#Read the config file to get the key
	home = os.path.expanduser('~')
	configfile = home+"/.pushbullet"
	if not os.path.isfile(configfile):
		print "You need to run the pushbullet_config.py script"
		sys.exit()

	config = ConfigParser.ConfigParser()
	config.read(configfile)
	key = config.get('Pushbullet','key')
	

	# Build the command string
	cmd = "curl --header 'Authorization: Bearer {}'".format(key)
	cmd += ''' -X POST https://api.pushbullet.com/v2/pushes --header 'Content-Type: application/json' --data-binary '{"type": "note", '''
	cmd += '"title": "{}", "body": "{}"'.format(title,message)
	cmd += "}' > /dev/null 2>&1"

	os.system(cmd)






	# if os.path.isfile(configfile) and force:
	# 	with open(configfile, 'w') as config:
	# 		config.write("[Pushbullet]\nkey={}\n".format(key))
	# elif os.path.isfile(configfile) and not force:
	# 	print "File exists, use the -f option to Overwrite"
	# 	sys.exit()

	# else:
	# 	with open(configfile, 'w') as config:
	# 		config.write("[Pushbullet]\nkey={}\n".format(key))

if __name__ == '__main__':
	main()