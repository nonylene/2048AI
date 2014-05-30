# -*- coding: utf-8 -*

import sys
import os
import time

u = int(input("URL(1:outside, 2:ring): "))
if u == 1:
	url = "2048.semantics3.com/"
elif u == 2:
	url = "ring:2048/"
else:
	print("ha????????")
	sys.exit()

mode = int(input("mode(1:normal, 2:beta, 3:nightly): "))
if mode > 3:
	print("ha????????")
	sys.exit()

count = int(input("やりたい回数: "))

if mode == 1:
	from kaeruze2048 import yaruze
	for i in range(0,count):
		print (str(i+1) + "回目" + "\n")
		yaruze(url)
	filex = open('shut.txt', mode = 'a')
	file = open("shutx.txt", mode ='r')
	filex.write("\n--normal\n")
	sumk = 0
	for line in file:
		kaz = line.split()
		for i in range(0,len(kaz)):
			filex.write(kaz[i] + " ")
		filex.write('\n')
		sumk = int(kaz[0]) + sumk
	filex.write("average: " + str(int(sumk / count)) + "\n" )
	file.close()
	os.remove('shutx.txt')
	filex.close()

elif mode == 2:
	from kaeruze2048hybrid import yaruze
	for i in range(0,count):
		print (str(i+1) + "回目" + "\n")
		yaruze(url)
	filex = open('shut.txt', mode = 'a')
	file = open("shuty.txt", mode ='r')
	filex.write("\n--hybrid\n")
	sumk = 0
	for line in file:
		kaz = line.split()
		for i in range(0,len(kaz)):
			filex.write(kaz[i] + " ")
		filex.write('\n')
		sumk = int(kaz[0]) + sumk
	filex.write("average: " + str(int(sumk / count)) + "\n" )
	file.close()
	os.remove('shuty.txt')
	filex.close()

elif mode == 3:
	from yaruze2048 import yaruze
	for i in range(0,count):
		print (str(i+1) + "回目" + "\n")
		yaruze(url)
	filex = open('shut.txt', mode = 'a')
	file = open("shutz.txt", mode ='r')
	filex.write("\n--hyb3\n")
	sumk = 0
	for line in file:
		kaz = line.split()
		for i in range(0,len(kaz)):
			filex.write(kaz[i] + " ")
		filex.write('\n')
		sumk = int(kaz[0]) + sumk
	filex.write("average: " + str(int(sumk / count)) + "\n" )
	file.close()
	os.remove('shutz.txt')
	filex.close()

else:
	print("ha????????")