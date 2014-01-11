#!/usr/bin/python

import sys, re
from util import *

fin = open('test_case.txt', 'r')
fout = open('test.html', 'w')

fout.write('<html><head><title>...</title><body>')

title = True
for block in blocks(fin):
	block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
	if title:
		fout.write('<h1>')
		fout.write(block)
		fout.write('</h1>')
		title = False
	else:
		fout.write('<p>')
		fout.write(block)
		fout.write('/<p>')
fout.write('</body></html>')

fin.close()
fout.close()
