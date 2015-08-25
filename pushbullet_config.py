#!/usr/bin/env python

import argparse
import os
import sys

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
Create pushbullet config file
'''

def main():
	#  Argument Parser
	parser = argparse.ArgumentParser(description='Create a pushbullet config file at ~/.pushbullet')

	# Key
	parser.add_argument('-k','--key',dest='key', help='Your pushbullet key', required=True)
	parser.add_argument('-f','--force', dest='force', action="store_true", help="Overwrite existing config")
	# Parse arguments
	args = parser.parse_args()
	key = args.key
	force = args.force

	#Write the config file
	home = os.path.expanduser('~')
	configfile = home+"/.pushbullet"
	if os.path.isfile(configfile) and force:
		with open(configfile, 'w') as config:
			config.write("[Pushbullet]\nkey={}\n".format(key))
	elif os.path.isfile(configfile) and not force:
		print "File exists, use the -f option to Overwrite"
		sys.exit()

	else:
		with open(configfile, 'w') as config:
			config.write("[Pushbullet]\nkey={}\n".format(key))

if __name__ == '__main__':
	main()