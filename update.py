#update.py
#Evan Hopkins

import os
import sys

def main():
	manifest = sys.argv[1]
	getManifest(manifest)
	parseManifest()

def parseManifest():
	read = open('manifest.txt')
	for lyne in read:
		lyne = lyne.rstrip()
		download(lyne)

def download(url):
	command = 'curl '+url+' -o temp'
	os.system(command)
	read = open('temp')
	fileName = read.readline()[1:].rstrip()
	command = 'mv temp '+fileName
	os.system(command)

def getManifest(manifest):
	command = 'curl '+manifest+' -o manifest.txt'
	os.system(command)

if __name__=='__main__':
	main()